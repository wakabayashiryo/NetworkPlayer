# selectorServer
---
Raspberry Media Player have selector for RCA jack.
this program control selector using GUI on web browser.

## installation procedure
1. connect terminal using ssh ,can do teraterm or linux terminal
2. clone this repository 
> git clone https://github.com/wakabayashiryo/selectorServer.git
3. install necessary packages for python3
> sudo apt-get -y install python3-rpi.gpio   
> sudo apt-get -y install python3-flask
4. add service for automatically run program
5. copy service files to root folder
> cp selectorServer/selector.service /etc/systemd/system
6. start service
> sudo systemctl daemon-reload   
> sudo systemctl start selector   
> sudo systemctl enable selector   
7. check running service
> sudo systemctl status selector
