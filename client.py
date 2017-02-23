#!/usr/bin/python3
# -*- coding: utf-8 -*-


import socket
import sys

import lib.init as Init
import lib.Client.Client as Client


init=Init.Init()
init.config_file='/home/leo/emualator/etc/device.conf'
init.read_config()
init.init_database()

client=Client.Client()
client.start()

sys.exit()


