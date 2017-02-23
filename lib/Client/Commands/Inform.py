import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser



class Inform():
    
    def __init__(self,http_client):
        self.http_client=http_client

    def do(self):
        init=Init.Init()
        inform_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_inform']).read()
        templater=Template(inform_str)

        query_params=init.database.session.query(db.Param.Param)
        params=query_params.all()
        params_hash={}
        for param in params:
            params_hash[param.name]=param

        query_param_tr69=init.database.session.query(db.Param.Param).filter(db.Param.Param.tr69_interface=='Y')
        param_tr69_interface=query_param_tr69.one()

        param_tr69_interface.value='192.168.206.3'

        inform_str_parse=templater.render(params=params_hash,cwmp_id=1,event='1 BOOT',date='2014-10-29T16:24:21+00:00',param_tr69_interface=param_tr69_interface)

        self.http_client.request(inform_str_parse)
        ret=self.http_client.response()
        self.http_client.request("")
        return 
        


        
        
