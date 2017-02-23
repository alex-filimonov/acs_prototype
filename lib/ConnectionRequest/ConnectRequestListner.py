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

       

    def start(self):
        login='rtk'
        password='rtk'
        secret_str=login+":"+password
        b64Val = base64.b64encode(secret_str.encode())
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.bind(('', 7547))
        serv_sock.listen(1)


        try:
            while 1:
                client_sock, client_addr = serv_sock.accept()
#                print('Пришел запрос от :', client_addr)
                self.logger.info ('Connection ....'+client_addr[0][0])
                data = client_sock.recv(1024)
                udata = data.decode("utf-8")
#                print ("Текст запроса:")
#                print (udata)
                self.logger.info (u'REQUEST:')
                self.logger.info (str(udata))
                if re.search(r'authorization: basic ',udata.lower()):
                    # проверка авторизации
                    if re.search(b64Val.decode("utf-8"),udata):
                        resp=b"HTTP/1.0 200\r\nServer: emulator\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n"
#                        print ("Текст ответа:")
#                        print (resp)
                        self.logger.info (u'RESPONSE:')
                        self.logger.info (resp)
                        client_sock.sendall(resp)

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
                else:
                    resp=b"HTTP/1.0 401 Unauthorized\r\nServer: emulator\r\nWWW-Authenticate: Basic realm=\"proxy\"\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
#                    print ("Текст ответа:")
#                    print (resp)
                    self.logger.info(u'RESPONSE:')
                    self.logger.info(resp)
                    client_sock.sendall(resp)

#                print ("Закрываю сокет")
#                print ("-----------------------------------------------------------\n\n")
                self.logger.info (u'close socket')
                
                client_sock.shutdown(0)
                client_sock.close()
        finally: serv_sock.close()
        

