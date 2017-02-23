
import app.init as Init
import app.layout 

# путь до стороннего ORM
import sys
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db


class device_command():
    def __init__(self):
        self.shema_dir=""
        self.init=Init.Init()
        self.input_data={}
        self.layout=app.layout.layout(self.init)


    def index(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value
        

        init=Init.Init()
        query_commands=init.database.session.query(db.DeviceCommand.DeviceCommand).filter(db.DeviceCommand.DeviceCommand.device_id==device_id).order_by(db.DeviceCommand.DeviceCommand.id.desc())
        commands=query_commands.all()
        content['device_commands']=commands
        return self.layout.render_ajax('/device_command/index.html',content=content)


    def power_on(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value
        init=Init.Init()
        command=db.DeviceCommand.DeviceCommand(device_id=device_id,command='power_on',status='wait')
        init.database.session.add(command)
        init.database.session.commit()
        return self.layout.redirect("/device_info/index?device_id="+device_id)

    def power_off(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value
        init=Init.Init()
        command=db.DeviceCommand.DeviceCommand(device_id=device_id,command='power_off',status='wait')
        init.database.session.add(command)
        init.database.session.commit()
        return self.layout.redirect("/device_info/index?device_id="+device_id)




