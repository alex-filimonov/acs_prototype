#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
import re
import pprint
import requests, base64
import logging


import lib.init as Init
import lib.ORM.db as db
import lib.ConnectionRequest.ConnectRequestListner as Listner




init=Init.Init()
init.config_file='/home/leo/emualator/etc/device.conf'
init.read_config()
init.init_database()

listner=Listner.ConnectRequestListner()
listner.deviced_id=1
listner.start()


sys.exit()


