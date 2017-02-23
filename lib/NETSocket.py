################################################
###############################################

import os
import sys
import signal
import time
import socket

class NETSocket():

    def __init__(self):
        self.connect = socket.socket()

    def open(self,ip,port):
        self.connect.connect( (ip, port) )

    def send_all(self,data):
        self.connect.sendall(data.encode()) 

    def read(self):
        req=b''
        self.connect.settimeout(1)
        data=b''
        try:
            data = self.connect.recv(1024)
        except socket.error:
            return data.decode("utf-8")
        while data:
            req+=data
            try:
                data = self.connect.recv(1024)
            except socket.error:
                break
        return req.decode("utf-8")

    def close(self):
        self.connect.close()

        

