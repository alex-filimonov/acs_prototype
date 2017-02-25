
import app.init as Init
import app.layout 

# путь до стороннего ORM
import sys
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db
import os
import re



class netlog():
    def __init__(self):
        self.shema_dir=""
        self.init=Init.Init()
        self.input_data={}
        self.layout=app.layout.layout(self.init)

    def client_log(self):
        content={}
        content['input_data']=self.input_data
        init=Init.Init()

        query_devices=init.database.session.query(db.Device.Device)
        devices=query_devices.all()
        content['devices']=devices

        init=Init.Init()
        dump_path=init.config['DUMP']['dump_dir']
        index=1
        all_files=os.listdir(path=dump_path)
        files_hash={}
        for file in all_files:
            if len(re.findall(r'client',file))>0:
                files_hash[file]=1

        index=1
        sort_file=[]
        while True:
            flag=False
            if 'client_request'+str(index)+'.dump' in files_hash:
#            if files_hash.has_key(['client_request'+str(index)+'.dump']):
                sort_file.append({'file_name':'client_request'+str(index)+'.dump','name':'Запрос от клиента к ACS'})
                flag=True
            if 'client_response'+str(index)+'.dump' in files_hash:
                sort_file.append({'file_name':'client_response'+str(index)+'.dump','name':'Ответ ACS клиенту'})
                flag=True
            if flag==False:
                break
            index=index+1
            if index>1000:
                break
        
        for file in sort_file:
            try:
                f=open(dump_path+'/'+file['file_name'],'r')
                line = f.readline()
                data=""
                while line:
                    data=data+line
                    line = f.readline()                
                f.close()
                data=re.sub(r'<','&lt',data)
                data=re.sub(r'>','&gt',data)
                file['data']=data
            except:
                pass
        
        content['client_log']=sort_file
        return self.layout.render_ajax('/netlog/client_log.html',content=content)
        


    def listner_log(self):
        content={}
        content['input_data']=self.input_data
        init=Init.Init()

        query_devices=init.database.session.query(db.Device.Device)
        devices=query_devices.all()
        content['devices']=devices

        init=Init.Init()
        dump_path=init.config['DUMP']['dump_dir']
        index=1
        all_files=os.listdir(path=dump_path)
        files_hash={}
        for file in all_files:
            if len(re.findall(r'listner',file))>0:
                files_hash[file]=1

        index=1
        sort_file=[]
        tmp=[]
        while True:
            flag=False
            if 'listner_requst'+str(index)+'.dump' in files_hash:
                sort_file.append({'file_name':'listner_requst'+str(index)+'.dump','name':'Запрос от клиента к ACS'})
                flag=True
            if 'listner_response'+str(index)+'.dump' in files_hash:
                sort_file.append({'file_name':'listner_response'+str(index)+'.dump','name':'Ответ ACS клиенту'})
                flag=True
            if flag==False:
                break
            index=index+1
            if index>1000:
                break
        
        for file in sort_file:
            try:
                f=open(dump_path+'/'+file['file_name'],'r')
                line = f.readline()
                data=""
                while line:
                    data=data+line
                    line = f.readline()                
                f.close()
                data=re.sub(r'<','&lt',data)
                data=re.sub(r'>','&gt',data)
                file['data']=data
            except:
                pass
        
        content['listner_log']=sort_file
        return self.layout.render_ajax('/netlog/listner_log.html',content=content)
        



    def index(self):
        content={}
        content['input_data']=self.input_data
        init=Init.Init()

        query_devices=init.database.session.query(db.Device.Device)
        devices=query_devices.all()

        content['devices']=devices

        return self.layout.all_render_html('/netlog/index.html',content=content)


