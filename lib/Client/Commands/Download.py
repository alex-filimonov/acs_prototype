import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser



class Download():
    
    def __init__(self,http_client):
        self.http_client=http_client

    def insert_command_download(self,device_id,url):
        init=Init.Init()
        device_command=db.DeviceCommand.DeviceCommand(device_id=device_id,command='download',status='wait',download_url=url)
        init.database.session.add(device_command)
        init.database.session.commit()
        

    def do(self):
        init=Init.Init()
        download_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_download']).read()
        templater=Template(download_str)
        download_parse=templater.render(cwmp_id=1)
        self.http_client.request(download_parse)
        try:
            for key in self.params.keys():
                if key.lower()=='url':
                    self.insert_command_download(1,self.params['URL'])
        except:
            pass

        return 
        


        
        
