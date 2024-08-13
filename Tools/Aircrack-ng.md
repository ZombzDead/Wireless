## Aircrack-ng Tool Suite
Aircrack is a suite of tools for 802.11a/b/g WEP and WPA cracking. It implements the best known cracking algorithms to recover wireless keys once enough encrypted packets have been gathered. . The suite comprises over a dozen discrete tools, including airodump (an 802.11 packet capture program), aireplay (an 802.11 packet injection program), aircrack (static WEP and WPA-PSK cracking), and airdecap (decrypts WEP/WPA capture files) 

https://www.aircrack-ng.org/

Aireplay-ng

    Aireplay-ng --fakeauth 10 -e <SSID> mon0

Airodump-ng

    $ sudo iwconfig wlan0 channel 1   (will put the card on channel one)
    $ sudo iwconfig                   (wlan0 now shows the Frequency of the specific channel)

    Make the card cycle through the channels. Airodump, by default, will hop through 2.4GHz channels. 
    
    To specify what channels to hop through:
    $ sudo airodump-ng --band bg mon0   (this will tell the Card to hop through the specified band) 

### MDK4
Proof-of-concept tool to exploit common IEEE 802.11 protocol weaknesses.
    https://github.com/aircrack-ng/mdk4
    
Initial Install

    $ sudo apt-get install pkg-config libnl-3-dev libnl-genl-3-dev libpcap-dev
    $ sudo git clone https://github.com/aircrack-ng/mdk4.git
    $ cd mdk4 
    $ make 
    $ sudo make install

Usage

    $ sudo mdk4 <interface> <attack_mode> [attack_options]
    $ sudo mdk4 <interface in> <interface out> <attack_mode> [attack_options]

