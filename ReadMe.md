## Kali VM Settings
    Hardware > USB Controller > Switch USB Compatibility to USB 3.1

### Enable Wifi Adapter

Plug in Wireless Card

    $ ifconfig -a    (to locate the wlan0)
    $ sudo ifconfig wlan0 up  (Alfa Card will flicker)
    $ iwconfig   (will show if wifi adapters are configured)
    $ lsusb (will show connected adapters on vm)

Stop programs that might interfere with network settings

    $ sudo service network-manager stop
    $ sudo killall-9 dhclient wpa_supplicant

Take down wireless adapter for settings changes

    $ sudo ifconfig wlan0 down

Spoof the MAC address (recommended)

    $ sudo macchanger -m 00:11:22:33:44:55 wlan0 

Increase transmit power (recommended)  

    $ iw reg set BO
    $ iwconfig wlan0 txpower 30

Bring the interface back up to apply changes

    $ sudo ifconfig wlan0 up

### Configure Wlan for Monitor Mode

    $ sudo iw dev wlan0 del
    $ sudo iw phy phy0 interface add wlan0mon type monitor
    $ iw dev wlan0mon info
    $ ifconfig wlan0mon 

Or

    $ sudo airmon-ng    (will show the available list of Wlan interfaces)
    
    Place Card into "Monitoring Mode"
    $ sudo airmon-ng start wlan0   (will give message that monitor mode enable on mon0)
    $ sudo airmon-ng    (will show wlan0 and mon0 interfaces)
