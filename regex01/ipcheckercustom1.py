#!/usr/bin/env python3

import urllib.request
import re
import os
import socket


def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127."):
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip

def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('utf-8')
    externalIP = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', requesty)
    return externalIP

print('Your public IP address is: ' + str(get_external_ip()) )
print('Your local IP address is: ' + str(get_lan_ip() )

