
import app.init as Init
import app.layout 

# путь до стороннего ORM
import sys
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db


class device_info():
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
        query_devices=init.database.session.query(db.Device.Device).filter(db.Device.Device.id==device_id)
        device=query_devices.one()
        content['device']=device
        return self.layout.render_ajax('/device_info/index.html',content=content)


