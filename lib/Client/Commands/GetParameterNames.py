import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser
import sys



class GetParameterNames():
    
    def __init__(self,http_client):
        self.http_client=http_client
        self.params=None


    def do(self):
        init=Init.Init()

        ret_values=[]

        try:
            for param_name_key in self.params.keys():
                if param_name_key.lower()=='parameterpath':
                    
                    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

                    param_name=self.params[param_name_key]
                    print (param_name)
                    query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.name.like(param_name+'%'))
                    params=query_params.all()
                    ret_values=ret_values+params
                    
        except:
            pass
        get_parameter_names_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_get_parameter_names']).read()
        templater=Template(get_parameter_names_str)
        content=templater.render(params=ret_values,leng=len(ret_values),cwmp_id=1)
        self.http_client.request(content)
        return 

        


        
        
