################################################
###############################################

import re
import sys

import app.init as Init
import importdir
import traceback
import app.layout as layout




class Controller():

    def __init__(self):
        self.shema_dir=""
        self.Controller=""
        self.Action=""
        init=Init.Init()
        init.config_file='/home/leo/emualator/web/app/etc/site.conf'
        init.read_config()
        init.init_database()
        importdir.do(init.config['CONTROLLERS']['controller_dir'], globals())

    def get_controller(self,controller_name):
        if controller_name=='default':
            return default.default()
        if controller_name=='device_info':
            return device_info.device_info()
        if controller_name=='device_command':
            return device_command.device_command()
        if controller_name=='param':
            return param.param()
        return None

    def parser_url(self,url):
        result_parse=re.split(r'/',url)
        if len(result_parse)>2:
            return {'controller':result_parse[1],'action':result_parse[2]}
        if len(result_parse)>1:
            return {'controller':result_parse[1],'action':None}
        return {'controller':None,'action':None}

    def do(self,input_data):
        # тут меняем логику если надо
        init=Init.Init()
        output=""
        try:
            request_url=input_data['env']['REDIRECT_URL']
            path=self.parser_url(request_url)
            if path['controller']==None or path['action']==None:
                cntrl=default.default()
                cntrl.input_data=input_data
                l=layout.layout(init)
                return l.redirect("./default/index")
           
            control_str=path['controller']
            action_str=path['action']

            ctrl=self.get_controller(control_str)
            ctrl.input_data=input_data
            mtd=getattr(ctrl,action_str)
            return mtd()

        except Exception:
            e = sys.exc_info()
            str=traceback.format_exc()
            err=error.error(input_data,str)
            output=err.index()
        return output
        

