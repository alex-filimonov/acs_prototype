import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser



class FactoryReset():
    
    def __init__(self,http_client):
        self.http_client=http_client

    def insert_command_factory_reset(self,device_id):
        init=Init.Init()
        device_command=db.DeviceCommand.DeviceCommand(device_id=device_id,command='factory_reset',status='wait')
        init.database.session.add(device_command)
        init.database.session.commit()
        

    def do(self):
        init=Init.Init()
        factory_reset_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_factory_reset']).read()
        templater=Template(factory_reset_str)
        factory_reset_parse=templater.render(cwmp_id=1)
        self.http_client.request(factory_reset_parse)
        self.insert_command_factory_reset(1)

        return 
        


        
        
