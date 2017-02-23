#!/usr/bin/python3
# -*- coding: utf-8 -*-

# тестовый клиент
import socket
import sys
import lib.Parser as Parser
import re
import lib.init as Init
import lib.ORM.db as db


try:
    print ("in try")
    a['we']=3545
except Exception:
    print ("BUGS")
    e = sys.exc_info()
    print (e)

    obj=e[2]
    for o in obj:
       print (o)



sys.exit()

init=Init.Init()
init.config_file='/home/leo/emualator/etc/device.conf'
init.read_config()
init.init_database()


#device_command=db.DeviceCommand.DeviceCommand(device_id=1,command='reboot',status='wait')
#init.database.session.add(device_command)
#init.database.session.commit()
#sys.exit()

xml="""
<soap:Envelope
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
 xmlns:cwmp="urn:dslforum-org:cwmp-1-1">
<soap:Header>
</soap:Header>
<soap:Body>
<cwmp:GetParameterNames>
<ParameterPath>InternetGatewayDevice.DeviceInfo.Hello</ParameterPath>
<NextLevel>false</NextLevel>
</cwmp:GetParameterNames>
</soap:Body>
</soap:Envelope>
"""

parse=Parser.Parser()
commands_server=parse.parse_struct(xml)

for command in commands_server.keys():
  if re.search(r'getparameternames',command.lower()):
        print (command)
        params=commands_server[command]

        print (params['ParameterPath'])


    
    





