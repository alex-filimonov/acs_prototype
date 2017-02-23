#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
import re
import pprint
import requests, base64
import time
from sqlalchemy.orm import Session
import lib.ConnectionRequest.ConnectRequestListner as Listner


import lib.init as Init
import lib.ORM.db as db
import lib.device as device


init=Init.Init()
init.config_file='/home/leo/emualator/etc/device.conf'
init.read_config()
init.init_database()

init.log_info("Start device emualator ...")
device=device.Device()

while 1:
    init.database.session.close_all()
    init.database.session=Session(bind=init.database.engine)
    query_commands=init.database.session.query(db.DeviceCommand.DeviceCommand).filter(db.DeviceCommand.DeviceCommand.status.in_(['wait','processing']))
    commands=query_commands.all()
    for command in commands:
        print ("Исполняю команду "+command.command)
        device.do(command)
    time.sleep(int(init.config['DEVICE']['time_refresh']))



