# How does it work:
While sending a one-byte message "\x00" to any of these amazon servers they return a message "Access Denied". On the surface it's simple, however this can be an issue 

# Servers Affected: ~8,700

# Vulnerable Payload: \x00 - Null byte

# Amplification Factor: 37x

# How I Found It:
While looking for an amplification attack in the TwinCAT service, I stumbled across around 8,700 amazon servers that are all vulnerable to the same amplification attack. This attack works by sending a single one byte packet over UDP to any port, and the server then responds "Access Denied". Although you don't actually get into the server, this still has an amplification factor of 37x, as the one byte message you sent gets transformed into a 37 byte return. However, what's even more concerning than the amplification method is the source at which its coming from. Amazon servers could be whitelisted under certain firewalls, unlike other commonly seen amplification attacks such as LDAP and DNS. Also, the source port is changeable as well so it can't be blocked as easily as the other methods.

This vulnerability merely demonstrates how something as simple as returning a message "Access Denied" could be transformed into fuel for a malicious attack. There is also an attached code example of what an attackers script would look like if they were to turn this into an amplification attack.
