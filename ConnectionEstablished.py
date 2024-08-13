### Disable monitor mode / Enable managed mode:
    $ ifconfig wlan0 down
    $ airmon-ng stop wlan0
    $ iwconfig wlan0 mode managed
    $ ifconfig wlan0 up

### Connect to a specific access point on the network:
    $ iwconfig wlan0 essid $ESSID ap $bssid
    
### Connect to ANY access point on the network:
    $ iwconfig wlan0 essid $ESSID ap any  

### Connect using WEP:
    $ iwconfig wlan0 essid $ESSID key $PASSWORD && dhclient wlan0  

### Connect using WPA/WPA2:
    1. Stop interfering programs (see setup).
    2. Create wpa_supplicant.conf:
      $ wpa_passphrase $ESSID $PASSWORD > wpa_supplicant.conf
    3. Connect to the network.
      $ wpa_supplicant -cwpa_supplicant.conf -iwlan0 -B && dhclient wlan0 
