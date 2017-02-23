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



init=Init.Init()
init.config_file='/home/leo/emualator/etc/connection_request.conf'
init.read_config()
init.init_database()

query=init.database.session.query(db.User.User)
users=query.all()
for user_item in users:
    print (user_item.id)



sys.exit()


