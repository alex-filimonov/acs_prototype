#!/usr/bin/python3
# -*- coding: utf-8 -*-

# первый тестовый скрипт
import socket
import sys
import re
import pprint


print ("Тест вывода")

result = re.search(r'Vi', 'AV Analytics Vidhya AV')
print (result)


str1="hello aleX Test regexp 45 232"
if re.search(r'alex te',str1.lower()):
    print ("Нашел")
else:
    print ("Не нашел")



