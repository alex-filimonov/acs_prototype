#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests, base64
import re

print ("Тестируем base64")

b64Val = base64.b64encode(b"rtk:rtk1")

print (b64Val)


print ("Test regexp")

str1='''GET /fgfdg HTTP/1.1
TE: deflate,gzip;q=0.3
Keep-Alive: 300
Connection: Keep-Alive, TE
Authorization: Basic cnRrOnJ0aw==
Host: 192.168.206.3:7547
User-Agent: libwww-perl/6.18
'''


if re.search(b64Val.decode("utf-8"),str1):
    print ("Аунтификация успешно пройдено")
else:
    print ("Ничего не нашел")








