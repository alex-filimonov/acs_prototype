################################################
# main db class
#  Alksey Filimonov
# docs
# http://lectureswww.readthedocs.io/6.www.sync/2.codding/9.databases/2.sqlalchemy/3.orm.html
###############################################

from sqlalchemy import create_engine    
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, MetaData
from sqlalchemy import orm
from sqlalchemy.orm import Session,sessionmaker
from lib import importdir

class DB():

    def __init__(self):
        self.shema_dir=""
    def set_shema_dir(self,dir):
        self.shema_dir=dir

    def initDataBaseEngine(self,host,driver,database,login,password,debug_on):
        self.engine=create_engine(driver+"://"+login+":"+password+"@"+host+"/"+database,echo=debug_on)
        self.meta = MetaData(bind=self.engine, reflect=True)
        
        self.session = Session(bind=self.engine)
        importdir.do(self.shema_dir, globals())
        return

        
        

        
