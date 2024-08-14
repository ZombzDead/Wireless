## Kali VM Settings
    Hardware > USB Controller > Switch USB Compatibility to USB 3.1

### Enable Wifi Adapter
    https://docs.alfa.com.tw/Product/AWUS036ACM/
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

### Alfa Adapter Troubleshooting
    https://kali.download/kali/pool/main/l/linux/ 
    Install the following:
    $ sudo dpkg -i linux-headers-6.5.0-kali3-common_6.5.6-1kali1_all.deb
    $ sudo dpkg -i linux-kbuild-6.5.0-kali3_6.5.6-1kali1_amd64.deb
    $ sudo dpkg -i linux-compiler-gcc-13-x86_6.5.6-1kali1_amd64.deb 
    $ sudo dpkg -i linux-headers-6.5.0-kali3-amd64_6.5.6-1kali1_amd64.deb  
    
    $ cd /rt18814au
    $ Sudo make
    
    After installing firmware and drivers reattempt to setup the WLAN interface (Reboot may be required)

## Tips
 IDENTIFY AND CRACK ENCRYPTION - Use the access point's MAC address to find the manufacturer. Then search by manufacturer or ESSID exploits and default wireless keys for that model.
 
 Wireless Scanning Tools - Airsnarf, Airsnort, BdAddr, Bluesnarfwer, Btscanner, FakeAP, GFI LANguard, WifiTAP, GPSdrive, Kismet, and macchanger

 Additional Softwared - Raspberry Pi (https://www.raspberrypi.com/software/) & Pineapple (https://soliloquyforthefallen.net/?cat=109)
 
 
