# selectorServer
---
Raspberry Media Player have selector for RCA jack.
this program control selector using GUI on web browser.
## STEP1 installation volumio OS [on windows]
[reference site](https://itdecoboconikki.com/2017/02/10/2017volumio-2041install/)
1. download image file of leatest volumio   
2. format SD card using SD CardFormatter    
3. write image file to SD card using Win32DiskImager   
4. connect raspberry pi to power and ethernet and insert SD card
5. awhile, access http://volumio.local [in local net]
6. using browser set configration of volumio   
[setting guide for using hardware](http://www.raspberrypiwiki.com/index.php/File:RPI-HIFI-DAC-manual-en.pdf)
7. go to setting selector server    
**If you can not access the volumio,using application to serach IP address **

## STEP2 installation selectorserver [on Linux]
1. access to http://volumio.local/dev and enable SSH.
1. connect terminal using ssh ,can do by teraterm or linux terminal
2. clone this repository 
> git clone https://github.com/wakabayashiryo/selectorServer.git
3. install necessary packages for this program on python3
> sudo apt-get -y install python3-rpi.gpio   
> sudo apt-get -y install python3-flask
4. add service for automatically run program
5. copy service files to system folder
> cp selectorServer/selector.service /etc/systemd/system
6. start service and enable to automatically run
> sudo systemctl daemon-reload   
> sudo systemctl start selector   
> sudo systemctl enable selector   
7. check running service
> sudo systemctl status selector
8. reboot
