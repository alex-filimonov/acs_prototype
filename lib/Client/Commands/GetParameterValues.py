import lib.init as Init
import lib.ORM.db as db
from jinja2 import Template
import lib.Parser as Parser
import sys



class GetParameterValues():
    
    def __init__(self,http_client):
        self.http_client=http_client
        self.params=None


    def do(self):
        init=Init.Init()

        ret_values=[]

        param_names=self.params['ParameterNames']
        for param_name in param_names:
            if param_name=='string':
                if type(self.params['ParameterNames'][param_name])==str:
                    query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.name.like(self.params['ParameterNames'][param_name]+'%'))
                    params=query_params.all()
                    ret_values=ret_values+params
                else:
                    for find_param in self.params['ParameterNames'][param_name]:
                        query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.name.like(find_param+'%'))
                        params=query_params.all()
                        ret_values=ret_values+params

        get_parameter_values_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_get_parameter_values']).read()
        templater=Template(get_parameter_values_str)

        content=templater.render(params=ret_values,leng=len(ret_values),cwmp_id=1)


        self.http_client.request(content)
        return 
        


        
        
