################################################
# Connection Request Listner class
#  Alksey Filimonov
###############################################

import socket
import sys
import re
import pprint
import requests, base64
import lib.ORM.db as db
import lib.init as Init
import logging
import logging.handlers
import time
import os
import traceback

class ConnectRequestListner():
    
    def __init__(self):
        self.shema_dir=""
        self.database=db.DB()
        init=Init.Init()
        self.database.set_shema_dir(init.config['ORM']['shema_files'])
        self.database.initDataBaseEngine(init.config['DATABASE']['host'],init.config['DATABASE']['driver'],init.config['DATABASE']['database'],init.config['DATABASE']['login'],init.config['DATABASE']['password'],False)
        self.logger=logging.getLogger()
        self.logger.setLevel(int(init.config['CONNECT_REQUEST']['log_level']))
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler = logging.FileHandler(init.config['CONNECT_REQUEST']['log_file'])
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info (u'Connection request ..... init' )
        self.index=1
        self.dump_path=''

    def erase_dump(self):
        init=Init.Init()
        dump_path=init.config['DUMP']['dump_dir']
        self.index=1
        self.dump_path=dump_path
        files=os.listdir(path=dump_path)
        for file in files:
            if len(re.findall(r'listner',file))>0:
                os.remove(dump_path+'/'+file)
    
    def write_dump(self,file_templater,data):
        try:
            f=open(self.dump_path+'/listner_'+file_templater+str(self.index)+".dump",'w')
            f.write(data)
            f.close()
            self.index=self.index+1
            print (self.dump_path)
            print (self.dump_path+'/listner_'+file_templater+str(self.index)+".dump")
        except Exception:
            e = sys.exc_info()
            str1=traceback.format_exc()
            print (str1)

    def start(self):
        
        time.sleep(int(1))
        self.erase_dump()


        login='rtk'
        password='rtk'
        port=7547

        query_device=self.database.session.query(db.Device.Device).filter_by(id=1)
        devices=query_device.all()
        device=None
        if len(devices)==0:
            self.logger.info (u'Not detect device model' )
            return
        device=devices[0]
        

        try:
            query_param=self.database.session.query(db.Param.Param).filter_by(name='InternetGatewayDevice.ManagementServer.ConnectionRequestUsername')
            param=query_param.one()
            login=param.value
            query_param=self.database.session.query(db.Param.Param).filter_by(name='InternetGatewayDevice.ManagementServer.ConnectionRequestPassword')
            param=query_param.one()
            password=param.value
            query_param=self.database.session.query(db.Param.Param).filter_by(name='InternetGatewayDevice.ManagementServer.ConnectionRequestURL')
            param=query_param.one()
            url=param.value
            if len(re.findall(r':\d+',url))>0:
                k1=re.findall(r':\d+',url)[0]
                if len(re.findall(r'\d+',k1))>0:
                    port=re.findall(r'\d+',k1)[0]
        except:
            device.listner_connect_request="Error start - not read param"
            self.database.session.commit()
            return 
            



        secret_str=login+":"+password
        b64Val = base64.b64encode(secret_str.encode())

        serv_sock=None
        try:
            serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv_sock.bind(('', int(port)))
            serv_sock.listen(1)
            self.logger.info (u'Connection request ..... run' )
            device.listner_connect_request="Started"
            self.database.session.commit()
        except Exception:
            e = sys.exc_info()
            str=traceback.format_exc()
            print (str)
            device.listner_connect_request="Error start"
            self.database.session.commit()
            self.logger.info (u'Connection request ..... fail' )
            self.logger.info (str )
            return

        try:
            while 1:
                client_sock, client_addr = serv_sock.accept()
#                print('Пришел запрос от :', client_addr)
                self.logger.info ('Connection ....'+client_addr[0][0])
                data = client_sock.recv(1024)
                udata = data.decode("utf-8")
#                print ("Текст запроса:")
#                print (udata)
                self.write_dump('requst',udata)
                self.logger.info (u'REQUEST:')
                self.logger.info (udata)
                if re.search(r'authorization: basic ',udata.lower()):
                    # проверка авторизации
                    if re.search(b64Val.decode("utf-8"),udata):
                        resp=b"HTTP/1.0 200\r\nServer: emulator\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"
#                        print ("Текст ответа:")
#                        print (resp)
                        self.logger.info (u'RESPONSE:')
                        self.logger.info (resp)
                        client_sock.sendall(resp)
                        self.write_dump('response',resp.decode('utf-8'))

                        command=db.DeviceCommand.DeviceCommand(device_id=1,command='connect_request',status='wait')
                        self.database.session.add(command)
                        self.database.session.commit()
                        # запуск tr клиента по connect_request

                    else:
                        resp=b"HTTP/1.0 401 Unauthorized\r\nServer: emulator\r\nWWW-Authenticate: Basic realm=\"proxy\"\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
#                        print ("Текст ответа:")
#                        print (resp)
                        self.logger.info (u'RESPONSE:')
                        self.logger.info (resp)
                        client_sock.sendall(resp)
                        self.write_dump('response',resp)
                else:
                    resp=b"HTTP/1.0 401 Unauthorized\r\nServer: emulator\r\nWWW-Authenticate: Basic realm=\"proxy\"\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
#                    print ("Текст ответа:")
#                    print (resp)
                    self.logger.info(u'RESPONSE:')
                    self.logger.info(resp)
                    client_sock.sendall(resp)
                    self.write_dump('response',resp.decode('utf-8'))

#                print ("Закрываю сокет")
#                print ("-----------------------------------------------------------\n\n")
                self.logger.info (u'close socket')
                
                client_sock.shutdown(0)
                client_sock.close()
        except Exception:
            e = sys.exc_info()
            str=traceback.format_exc()
            print (str)
        finally: 
            serv_sock.close()
        

