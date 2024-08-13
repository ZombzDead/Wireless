## Kismet is a wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework. (Reconnaissance Tool)

https://www.kali.org/tools/kismet/

Initial Install of Kismet

    Install the dependencies for Kismit:
    $ sudo apt install build-essential git libmicrohttpd-dev pkg-config zlib1g-dev libnl-3-dev libnl-genl-3-dev libcap-dev libpcap-dev libnm-dev libdw-dev libsqlite3-dev libprotobuf-dev libprotobuf-c-dev protobuf-compiler protobuf-c-compiler libsensors4-dev libusb-1.0.0-dev python3 python3-setuptools python3-protobuf python3-requests python3-numpy python3-serial python3-usb python3-dev librtlsdr0
    
    $ git clone https://www.kismetwireless.net/git/kismet.git 
    $ cd kismet 
    $ git pull 
    $ ./configure 
    $ make 
    $ make -j$(nproc) 
    
    $ sudo make suidinstall 
    $ sudo usermod -aG kismet $USER 

Run Kismet

    $ kismet
    Point your browser at http://localhost:2501
    	set username/password in browser
	Data source > Available Interfaces > Select interface
