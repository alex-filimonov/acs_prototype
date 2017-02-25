################################################
###############################################

import os
import sys
import signal
import time
import lib.NETSocket as socket
import re


class HTTPClient():

    def __init__(self):
        self.connect = socket.NETSocket()
        self.http_user_agent="Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"
        self.http_connection="keep-alive"
        self.http_host="example.com"
        self.http_accept='text/html'
        self.index=1
        self.dump_path=''
        self.dump_main_templater='client_'

    def open(self,ip,port):
        self.connect.open( ip, port )

    def get_http_header(self,data):
        return "GET / HTTP/1.1\r\nHost: "+self.http_host+"\r\nContent-Length: "+str(len(data))+"\r\nUser-Agent: "+self.http_user_agent+"\r\nAccept: "+self.http_accept+"\r\nConnection: "+self.http_connection+"\r\n\r\n"

    def request(self,data):
        req=self.get_http_header(data)
        req=req+data
        print (req)
        self.connect.send_all(req)
        self.write_dump('request',req)

    def response_full(self):
        resp=self.connect.read()
        print (resp)
        self.write_dump('response',resp)
        return resp

    def response(self):
        resp=self.connect.read()
        print (resp)
        data=re.split(r'\r\n\r\n',resp)
        if len(data)>1:
            self.write_dump('response',data[1])
            return data[1]
        return ""

    def close(self):
        self.connect.close()

    def write_dump(self,file_templater,data):
        f=open(self.dump_path+'/'+self.dump_main_templater+file_templater+str(self.index)+".dump",'w')
        f.write(data)
        f.close()
        self.index=self.index+1

