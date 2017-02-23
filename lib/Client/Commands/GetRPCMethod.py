import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser
import sys



class GetRPCMethod():
    
    def __init__(self,http_client):
        self.http_client=http_client
        self.params=None


    def do(self):
        init=Init.Init()

        ret_values=[]

        get_parameter_values_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_get_rpc_method']).read()
        templater=Template(get_parameter_values_str)

        content=templater.render(leng=len(ret_values),cwmp_id=1)


        self.http_client.request(content)
        return 
        


        
        
