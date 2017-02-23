
import lib.init as Init
import lib.ORM.db as db
import re
import lib.HTTPClient as HTTPClient
import lib.Parser as Parser
import lib.Client.Commands.Inform as Inform
import lib.Client.Commands.GetParameterValues as GetParameterValues
import lib.Client.Commands.SetParameterValues as SetParameterValues
import lib.Client.Commands.GetRPCMethod as GetRPCMethod
import lib.Client.Commands.Reboot as Reboot
import lib.Client.Commands.FactoryReset as FactoryReset
import lib.Client.Commands.Download as Download
import lib.Client.Commands.GetParameterNames as GetParameterNames



class Client():
    def __init__(self):
        self.acs_full_url=None
        self.acs_ip=None
        self.acs_port=None
        self.http=HTTPClient.HTTPClient()

    def get_acs_url(self):
        init=Init.Init()
        url=None
        try:
            query_param=init.database.session.query(db.Param.Param).filter_by(name='InternetGatewayDevice.ManagementServer.URL')
            param_url=query_param.one()
            url=param_url.value
            self.acs_full_url=url
        except BaseException :
            pass
        if url:
            port=None
            ip=None
            if len(re.findall(r'\d+.\d+.\d+.\d+',url))>0:
                ip=re.findall(r'\d+.\d+.\d+.\d+',url)[0]
            if len(re.findall(r':\d+',url))>0:
                port=re.findall(r'\d+',re.findall(r':\d+',param_url)[0])
            else:
                port=80
            self.acs_ip=ip
            self.acs_port=port
            return (ip,port)
        return (None,None)

    def get_command(self):
        ret=self.http.response()
        parse=Parser.Parser()
        data=parse.parse_struct(ret)
        return data
        

    def start(self):
        (acs_server_ip,acs_server_port)=self.get_acs_url()

        if acs_server_ip==None:
            print ("Client STOP .... nod found ACS_URL")
            return
        self.http.open(self.acs_ip,self.acs_port)
        print ("Open",acs_server_ip,acs_server_port)

        inform=Inform.Inform(self.http)
        inform.do()
        break_command=False
        while True:
            commands_server=self.get_command()
            if commands_server==None:
                break
            if break_command==True:
                break
            for command in commands_server.keys():
                if re.search(r'getparametervalues',command.lower()):
                    method=GetParameterValues.GetParameterValues(self.http)
                    method.params=commands_server[command]
                    method.do()
                if re.search(r'getrpcmethod',command.lower()):
                    method=GetRPCMethod.GetRPCMethod(self.http)
                    method.params=commands_server[command]
                    method.do()
                if re.search(r'getparameternames',command.lower()):
                    method=GetParameterNames.GetParameterNames(self.http)
                    method.params=commands_server[command]
                    method.do()
                if re.search(r'setparametervalues',command.lower()):
                    method=SetParameterValues.SetParameterValues(self.http)
                    method.params=commands_server[command]
                    method.do()
                if re.search(r'reboot',command.lower()):
                    method=Reboot.Reboot(self.http)
                    method.params=commands_server[command]
                    method.do()
                    break_command=True
                if re.search(r'factoryreset',command.lower()):
                    method=FactoryReset.FactoryReset(self.http)
                    method.params=commands_server[command]
                    method.do()
                    break_command=True
                if re.search(r'download',command.lower()):
                    method=Download.Download(self.http)
                    method.params=commands_server[command]
                    method.do()
                    break_command=True
        
        self.http.close()
        return 

        

