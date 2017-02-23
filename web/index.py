#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cgi
import sys
import app.Controller as Controller
import cgitb
#cgitb.enable()


input_data={}
input_data['env']=os.environ
input_data['cgi']=cgi.FieldStorage()

controller=Controller.Controller()
out=controller.do(input_data)
print(out)
sys.exit()


