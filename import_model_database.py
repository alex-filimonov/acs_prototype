#!/usr/bin/python3
# -*- coding: utf-8 -*-

# первый тестовый скрипт
import socket
import sys
import re
import pprint
import requests, base64
import logging
import binascii


import lib.init as Init
import lib.ORM.db as db



init=Init.Init()
init.config_file='/home/leo/emualator/etc/import_model_database.conf'
init.read_config()
init.init_database()



logging.info (u'Read file ...' + init.config['IMPORT_DATA']['model_data_file'] )

data_file=open(init.config['IMPORT_DATA']['model_data_file'],'r')

for line in data_file:
    line=re.sub("\n","",line)
    if len(line)>0:
        fields=re.split("\t",line)
        if len(fields)>2:
            

            fields[0]=re.sub(r'[\x7F-\xFF]',"",fields[0])
            fields[1]=re.sub(r'[\x7F-\xFF]',"",fields[1])
            fields[2]=re.sub(r'[\x7F-\xFF]',"",fields[2])
            fields[3]=re.sub(r'[\x7F-\xFF]',"",fields[3])
            is_write='N'
            if fields[2]=="1":
                is_write='Y'
            param=db.Param.Param(device_id=init.config['IMPORT_DATA']['device_id'],id=binascii.crc32(fields[0].encode()),name=fields[0],isWrite=is_write,value=fields[1],type=fields[3])
            param_default=db.ParamDefault.ParamDefault(device_id=init.config['IMPORT_DATA']['device_id'],id=binascii.crc32(fields[0].encode()),name=fields[0],isWrite=is_write,value=fields[1],type=fields[3])
            init.database.session.add(param)
            init.database.session.add(param_default)

device=db.Device.Device(id=init.config['IMPORT_DATA']['device_id'],name=init.config['IMPORT_DATA']['device_name'],status='off')
init.database.session.add(device)
init.database.session.commit();

data_file.close()
