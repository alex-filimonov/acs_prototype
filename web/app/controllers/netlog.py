
import app.init as Init
import app.layout 

# путь до стороннего ORM
import sys
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db



class netlog():
    def __init__(self):
        self.shema_dir=""
        self.init=Init.Init()
        self.input_data={}
        self.layout=app.layout.layout(self.init)


    def index(self):
        content={}
        content['input_data']=self.input_data
        init=Init.Init()

        query_devices=init.database.session.query(db.Device.Device)
        devices=query_devices.all()

        content['devices']=devices

        return self.layout.all_render_html('/netlog/index.html',content=content)


