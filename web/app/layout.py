
from jinja2 import Template
import io


class layout():
    def __init__(self,init):
        self.shema_dir=""
        self.init=init

    def http_header(self):
        return "Content-Type: text/html;charset=utf-8\r\n\r\n"

    def local_render(self,view_path,content):
        ret=""
        with io.open(self.init.config['TEMPLATERS']['templater_dir']+view_path, "r", encoding="utf-8") as my_file:
            templater_file = my_file.read() 
            templater=Template(templater_file)
            ret=templater.render(content=content)
        return ret

    def redirect(self,url):
        return "Status: 302 Found\r\nLocation: "+url+"\r\n\r\n"

    def render_ajax(self,view_path,content):
        str=self.http_header()
        ret_str=""
        with io.open(self.init.config['TEMPLATERS']['templater_dir']+view_path, "r", encoding="utf-8") as my_file:
            templater_file = my_file.read() 
            templater=Template(templater_file)
            ret_str=templater.render(content=content,layout_content=content,view_path=view_path)
        return str+ret_str
            
    def all_render_html(self,view_path,content):
        str=self.http_header()
        view_controller=self.local_render(view_path,content)
        all_view=""
        with io.open(self.init.config['TEMPLATERS']['templater_dir']+'/layout.html', "r", encoding="utf-8") as my_file:
            templater_file = my_file.read() 
            templater=Template(templater_file)
            all_view=templater.render(content=view_controller,layout_content=content,view_path=view_path)

        return str+all_view
    

