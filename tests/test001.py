#!/usr/bin/python3
# -*- coding: utf-8 -*-

# первый тестовый скрипт
import socket
import sys
import re
import pprint
import requests, base64


login='rtk'
password='rtk'
secret_str=login+":"+password

b64Val = base64.b64encode(secret_str.encode())


print ("Тест сервера")


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('', 7547))
serv_sock.listen(1)


try:
    while 1:
        client_sock, client_addr = serv_sock.accept()
        print('Пришел запрос от :', client_addr)
        data = client_sock.recv(1024)
        udata = data.decode("utf-8")
        print ("Текст запроса:")
        print (udata)
        if re.search(r'authorization: basic ',udata.lower()):
            # проверка авторизации
            if re.search(b64Val.decode("utf-8"),udata):
                resp=b"HTTP/1.0 200\r\nServer: emulator\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"
                print ("Текст ответа:")
                print (resp)
                client_sock.sendall(resp)
            else:
                resp=b"HTTP/1.0 401 Unauthorized\r\nServer: emulator\r\nWWW-Authenticate: Basic realm=\"proxy\"\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
                print ("Текст ответа:")
                print (resp)
                client_sock.sendall(resp)
        else:
            resp=b"HTTP/1.0 401 Unauthorized\r\nServer: emulator\r\nWWW-Authenticate: Basic realm=\"proxy\"\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
            print ("Текст ответа:")
            print (resp)
            client_sock.sendall(resp)

        print ("Закрываю сокет")
        print ("-----------------------------------------------------------\n\n")
        client_sock.shutdown(0)
        client_sock.close()
finally: serv_sock.close()

sys.exit()


