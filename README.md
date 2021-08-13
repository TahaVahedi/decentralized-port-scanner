# decentralized-port-scanner
this tool can scan ports by connecting to a server. if server has enough clients(more than 3) this tools work.
and this tool work like down picture.
![work grapph Image](https://i.ibb.co/mHXr9P5/master.jpg)

### installation
if you want to test it on your localhost just do following steps:
```
  $ sudo git clone 
  $ cd decentralized-port-scanner
  $ python3 server/server.py 
```
then on another terminals run clients
```
  $ python3 scanner.py
```

-note: build.py make background.py start on os boot(linux, windows). but this is just for test and you should not do this.
