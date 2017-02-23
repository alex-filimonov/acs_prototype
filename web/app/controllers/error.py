
import app.init as Init
import app.layout 



class error():
    def __init__(self,input_data,err):
        self.shema_dir=""
        self.init=Init.Init()
        self.input_data=input_data
        self.error=err
        self.layout=app.layout.layout(self.init)


    def index(self):
        return self.layout.all_render_html('/error/index.html',self.error)
