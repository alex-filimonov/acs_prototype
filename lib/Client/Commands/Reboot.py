import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser



class Reboot():
    
    def __init__(self,http_client):
        self.http_client=http_client

    def insert_command_reboot(self,device_id):
        init=Init.Init()
        device_command=db.DeviceCommand.DeviceCommand(device_id=device_id,command='reboot',status='wait')
        init.database.session.add(device_command)
        init.database.session.commit()
        

    def do(self):
        init=Init.Init()
        reboot_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_reboot']).read()
        templater=Template(reboot_str)
        reboot_str_parse=templater.render(cwmp_id=1)
        self.http_client.request(reboot_str_parse)
        self.insert_command_reboot(1)

        return 
        


        
        
