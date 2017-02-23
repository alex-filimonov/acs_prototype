#!/usr/bin/python3
# -*- coding: utf-8 -*-

# первый тестовый скрипт
import socket
import sys
from jinja2 import Template


g={}

g['key']=45
g['key1']=45


html = open('./templater/t1.xml').read()
templater=Template(html)
html1=templater.render(name=u'Петя',gl=g)

print (html1)


