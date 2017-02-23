
import app.init as Init
import app.layout 

# путь до стороннего ORM
import sys
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db


class param():
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
        query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.device_id==device_id)
        params=query_params.all()
        content['params']=params
        return self.layout.render_ajax('/param/index.html',content=content)

    def index_all(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value

        init=Init.Init()
        query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.device_id==device_id)
        params=query_params.all()
        content['params']=params
        return self.layout.render_ajax('/param/all.html',content=content)

    def save_main(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value
        init=Init.Init()
        for param_key in content['input_data']['cgi'].keys():
            try:
                query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.device_id==device_id,db.Param.Param.name==param_key)
                param=query_params.one()
                param.value=content['input_data']['cgi'][param_key].value
            except:
                pass
        init.database.session.commit()
        return self.layout.redirect("/param/index?device_id="+device_id)

    def save(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value
        init=Init.Init()
        for param_key in content['input_data']['cgi'].keys():
            try:
                query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.device_id==device_id,db.Param.Param.name==param_key)
                param=query_params.one()
                param.value=content['input_data']['cgi'][param_key].value
            except:
                pass
        init.database.session.commit()
        return self.layout.redirect("/param/all?device_id="+device_id)


    def all(self):
        content={}
        content['input_data']=self.input_data
        device_id=content['input_data']['cgi']['device_id'].value

        init=Init.Init()
        query_params=init.database.session.query(db.Param.Param).filter(db.Param.Param.device_id==device_id).order_by(db.Param.Param.name)
        params=query_params.all()
        content['params']=params

        return self.layout.render_ajax('/param/all.html',content=content)

        
