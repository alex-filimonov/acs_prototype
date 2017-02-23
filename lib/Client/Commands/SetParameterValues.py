import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser
import sys



class SetParameterValues():
    
    def __init__(self,http_client):
        self.http_client=http_client
        self.params=None


    def save_param(self,data):
        init=Init.Init()
        name=data['Name']
        value=data['Value']['#text']
        query_param=init.database.session.query(db.Param.Param).filter_by(name=name)
        try:
            param=query_param.one()
            param.value=value
            init.database.session.commit()
        except:
            pass

    def do(self):
        init=Init.Init()
        try:
            if self.params['ParameterList']['ParameterValueStruct']:
                print (type(self.params['ParameterList']['ParameterValueStruct']))
                if type(self.params['ParameterList']['ParameterValueStruct'])==list:
                    for p in self.params['ParameterList']['ParameterValueStruct']:
                        self.save_param(p)
                        
                else:
                    p=self.params['ParameterList']['ParameterValueStruct']
                    self.save_param(p)
        except:
            pass

        set_parameter_values_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_set_parameter_values']).read()
        templater=Template(set_parameter_values_str)

        content=templater.render(cwmp_id=1)


        self.http_client.request(content)
        return 
        


        
        
