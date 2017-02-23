################################################
###############################################

import lib.init as Init
import lib.ConnectionRequest.ConnectRequestListner as Listner
import lib.ORM.db as db
import os
import sys
import signal
import time
import lib.Client.Client as Client


class Device():

#    def __init__(self):
#        self.shema_dir=""

    def connect_request(self,device,command):
        init=Init.Init()
        command.status='done'
        init.database.session.commit();
        client=Client.Client()
        client.start()

    def power_on(self,device,command):
        pid=os.fork()
        if pid==0:
            # дочерний процесс
            listner=Listner.ConnectRequestListner()
            listner.start()
            sys.exit()
        # родитель
        init=Init.Init()
        device.status="on"
        device.connect_request_pid=str(pid)
        init.database.session.commit()
        command.status='done'
        init.database.session.commit();
        try:
            client=Client.Client()
            client.start()
        except:
            pass


    def power_off(self,device,command):
        init=Init.Init()
        device.status="off"

        try:
            if int(device.connect_request_pid)>0:
                os.kill(int(device.connect_request_pid),signal.SIGTERM)
        except:
            pass
        device.connect_request_pid="0"
        init.database.session.commit()
        command.status='done'
        init.database.session.commit();


    def do(self,command):
        
        init=Init.Init()

        query_device=init.database.session.query(db.Device.Device).filter_by(id=1)
        devices=query_device.all()

        if len(devices)<1:
            command.status='error'
            init.database.session.commit()
            return
        if len(devices)>1:
            command.status='error'
            init.database.session.commit()
            return

        device=devices[0]
        if command.command=='power_on':
            self.power_on(device,command)
            return
        if command.command=='power_off':
            self.power_off(device,command)
            return

        if command.command=='connect_request':
            self.connect_request(device,command)
            return


        command.status='error'
        init.database.session.commit();


        
        

        
