# OpenVPN config manager

This is a simple but very useful WEB based config manager for OpenVPN, written in Python3 and Flask. Based on bulma CSS modern UI and Jinja2 HTML templates.

It can be used through SSH port forward channel or can be sit behind an authenticated Apache/Nginx (SSL) proxy.

## Main features

- create openvpn config,

- handle multiple servers (TCP, UDP..),

- download openvpn config,

- list separately revoked and valid configs,

- show config create and revoke dates,

- revoke config

## Setup

1. Download to /etc/openvpn/manager folder (git clone, etc..)

2. Edit manager.py: host, port, address, openvpn paths.  __IMPORTANT:__ for security resaons, it is highly recommended to keep service running on localhost (127.0.0.1)!

3. Create a service keeplaive crontab entry:

```
#openvpn manager keepalive
* * * * *       root    /etc/openvpn/manager/openvpn-manager.sh > /dev/null 2>&1
```

## Connect

Connect to manager from local PC to server through SSH tunnel:

```
ssh -i ~/.ssh/id_rsa -L 9090:localhost:5000 ubuntu@{remote.host.publicIP}
```

Then open in browser:

[http://127.0.0.1:9090](http://127.0.0.1:9090)






