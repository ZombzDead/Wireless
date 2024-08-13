## Bettercap
A powerful, easily extensible and portable framework written in Go which aims to offer to security researchers, red teamers and reverse engineers an easy to use, all-in-one solution with all the features they might possibly need for performing reconnaissance and attacking WiFi networks, Bluetooth Low Energy devices, wireless HID devices and Ethernet networks.

Main Features

  * WiFi networks scanning, deauthentication attack, clientless PMKID association attack and automatic WPA/WPA2 client handshakes capture.
  * Bluetooth Low Energy devices scanning, characteristics enumeration, reading and writing.
  * 2.4Ghz wireless devices scanning and MouseJacking attacks with over-the-air HID frames injection (with DuckyScript support).
  * Passive and active IP network hosts probing and recon.
  * ARP, DNS and DHCPv6 spoofers for MITM attacks on IP based networks.
  * Proxies at packet level, TCP level and HTTP/HTTPS application level fully scriptable with easy to implement javascript plugins.
  * A powerful network sniffer for credentials harvesting which can also be used as a network protocol fuzzer.
  * A very fast port scanner.
  * A powerful REST API with support for asynchronous events notification on websocket to orchestrate your attacks easily.
  * An easy to use web user interface.

https://www.bettercap.org/intro/

Initial Install

    Required Dependencies:
      libpcap
      libusb-1.0-0 (required by the HID module)
      libnetfilter-queue (on Linux only, required by the packet.proxy module)
  
      $ sudo apt update
      $ sudo apt install golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev
      $ go get -u github.com/bettercap/bettercap

 
Bettercap Commands 

    wifi.recon on              (Start 802.11 wireless base stations discovery and handshakes/PMKID capture)
    wifi.recon off             (Stop 802.11 wireless base stations discovery) 
    wifi.clear                 (Clear all access points collected by the WiFi discovery module)
    wifi.recon BSSID           (Set 802.11 base station address to filter for)
    
    wifi.assoc BSSID           (Send an association request to the selected BSSID in order to receive a RSN PMKID key) 
        (use all, * or ff:ff:ff:ff:ff:ff to iterate for every access point)
        
    wifi.deauth BSSID          (802.11 deauth attack, if an AP BSSID is provided, every client will be deauthenticated, otherwise only the selected client)
        (use all, * or ff:ff:ff:ff:ff:ff to deauth everything)
        
    wifi.show                  (Show current wireless stations list (default sorting by RSSI))
    
    wifi.show.wps BSSID        (Show WPS information about a given station) 
        (use all, * or ff:ff:ff:ff:ff:ff to select all)
        
    wifi.recon.channel CHANNEL (Comma separated list of channels to hop on.)
    wifi.recon.channel clear   (Enable channel hopping on all supported channels)
    
    wifi.ap                    (Inject fake management beacons in order to create a rogue access point)
        (requires wifi.recon to run )

