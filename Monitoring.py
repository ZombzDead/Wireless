### 1. Capture Wireless Traffic:
  # Start Wireshark
    $ sudo wireshark &
  # Start airodump-ng and log captured traffic to a file
    $ sudo airodump-ng wlan0 -w output-file-prefix
  # While capturing traffic with airodump, check that traffic to see if AP's support WPS.
    $ sudo wash -f output-file-prefix-*.cap

  # All-in-one w/web UI for monitoring traffic
    $ sudo kismet -c wlan0mon (Set username/password and save)

### 2. Generate Graph of Probe Requests of nearby Devices:
 # Generate graph of WiFi connections around (APs and clients connected to APs)
    $ airodump-ng -r targetnet.pcap -w TARGETNET 
    $ airgraph-ng -i TARGETNET-01.csv -g CAPR -o targetnet-connections.png

 # Generate graph of probe requests sent by devices around (Very interesting to rebuild devices' PNLs):
    $ airodump-ng -r targetnet.pcap -w TARGETNET 
    $ airgraph-ng -i TARGETNET-01.csv -g CPG -o targetnet-pnl.png

### 3. Find Hidden SSIDs (BSSID):
  # You must capture a Probe frame sent by a client machine as it connects to the network.
  # Passive: Wait. Eventually it will happen on its own and the ESSID will appear in either the top (access points) or bottom (clients) portion of the currently running airodump-ng.
    $ airodump-ng –c <channel> --bssid <MAC_AP> mon0
    $ aireplay-ng -0 20 –a <MAC_AP> mon0

### 4. Traffic Decryption
   $ sudo wireshark &   # requires PSK or PMK
   $ airdecap-ng -e <ESSID> -p <passphrase> <capture_pcap>
