# Information Disclosure Threat (AP/HotSpot Attacks)
Hotspot networks typically lack encryption in Layer 2 and higher, resulting in unencrypted transmitted network traffic. An attacker can record and observe the network traffic, potentially accessing confidential information. Weak protocols that do not include privacy functions, such as SMTP, POP3, HTTP, and most instant messaging protocols.  

Recommendation: To compensate for the lack of Layer 2 security, organizations need to implement more robust defenses at the upper layers. One way to limit the SSIDs that client devices connect to is by utilizing Group Policy functions and forbidding the connection to the "ANY" SSID. By doing so, end-users won't be able to connect to wireless networks that are not considered trustworthy. Educating users on the significance of confirming the identity of digital certificates before supplying sensitive information, ensuring that the root or issuing authority for the digital certificate is trusted.

# Over-Transmittal of Broadcast Range (Low)(AP/HotSpot Attacks)
The wireless access points are configured to extend the wireless signal beyond the organization's physical boundaries. When the wireless network's broadcast range is set too high, it becomes more vulnerable to potential threats due to its widespread accessibility. When the wireless network is more visible, attackers will attempt to compromise it from a further distance away, perhaps in a more concealed environment, remaining undetected.

Recommendation: Recommend reviewing and testing the transmit power levels of all APs to ensure their broadcast range is within the organization's boundaries. Implementing directional antennas will also help focus the RF energy on more defined areas of the facility instead of utilizing omnidirectional antennas that spread RF signals equally in all directions. Hiding SSIDs will also help.

# Session Hijacking (MAC Address Impersonation) (AP/HotSpot Attacks)
An attacker passively monitored the authorized users on the network and captured their IP and MAC addresses. This information allows attackers to track users who have shut down their systems without logging out. After monitoring an authenticated system, the attacker can determine when the system has stopped transmitting packets for a few minutes. Once identified, the attacker can impersonate the system's MAC and IP address and take control of the session.

  Attempt Successful - [network and captive portal]: An attacker could connect to the wireless network without authentication but did so with minimal access to resources. After connecting to the network, users are authenticated and granted internet access through a captive portal. After connecting to the network, the attacker ran an ARP Scan to gather a list of connected devices. By spoofing the MAC address of an authorized device, the attacker successfully bypassed the captive portal.
    
  Attempt Failed - [Passive sniffing, de-auth, blocked by required full authentication]: An attacker conducted spoofing attacks on the wireless networks to defeat the 802.1x authentication. By passively monitoring the wireless communications between the access points and connected clients, the attacker was able to discover and create a list of connected clients. This list included the MAC addresses of the connected clients. The attacker attempted to spoof the MAC address of those already authenticated devices by sending A de-authentication packet to the connected client, which caused the client to disconnect from the access point immediately. With the original client disconnected, the attacker attempted to connect to the access point using the spoofed MAC Address. 

Recommendation: Require either PSK authentication or utilizing AP Isolation.

# IEEE 802.11 MAC Attack (Bypass MAC Filtering)
The IEEE 802.11 MAC specification has a critical flaw in its design as it lacks a per-packet authentication mechanism. When an attacker transmits packets on 802.11 networks using a spoofed source MAC address, they can take on the identity of any node on the network, including the access point or any wireless station. This attack allows the attacker to exploit the trust relationship between the access point and the client stations on the network by sending frames with the source MAC address of the AP. The receiver of spoofed frames must process them as legitimate requests sent from the observed source MAC address.

    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 10 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ ifconfig wlan0mon down
    5. $ macchanger –-mac <VictimMac> wlan0mon
    6. $ ifconfig wlan0mon up
    7. $ aireplay-ng -3 –b <BSSID> -h <FakedMac> wlan0mon

# Weak/Default Passwords on Guest Wireless (Medium) (AP/HotSpot Attacks)
The passphrase for accessing the network is weak and easily guessed, which could compromise the system's security.

Recommendation: Configure the wireless network with a unique, robust, complex passphrase.

# VLAN Escaping (VLAN Hopping)
Many networks tend to have poor VLAN implementation or misconfigurations which could allow an attacker to exploit the VLAN trunking protocol to gain unauthorized access to other VLANs configured on the switch. Many switches are configured to utilize DTP (Dynamic Trunking Protocol) by default. DTP establishing a trunk link between two switches. An attacker conduct a few methods to attempt VLAN escaping.

Recommendation: It is recommended to implement 802.1x to regulate access to the network and to disable any unused ports. Keep the native VLAN of all trunk ports different from user VLANs and disable the use of DTP on the switches.

    https://github.com/nccgroup/vlan-hopping---frogger (Simple VLAN enumeration and hopping script. It is possible to hop vlans by abusing DTP protocol)
    $ git clone https://github.com/nccgroup/vlan-hopping.git
    $ chmod 700 frogger.sh
    $ ./frogger.sh
