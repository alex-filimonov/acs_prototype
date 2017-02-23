
#######################################################
# Init
# Aleksey Filimonov
#######################################################

import configparser
import logging

import sys
# ссылка на строний ORM
sys.path.append('/home/leo/emualator')
import lib.ORM.db as db



class Init(object):
    class __Init:
        def __init__(self):
            self.val = "Default data"
            self.config_file=None
            self.config=configparser.ConfigParser()
            self.database=None

        def __str__(self):
            return repr(self) + self.val

        def read_config(self):
            dataset=self.config.read(self.config_file)
            if len(dataset)<1:
                raise Exception("Config file not found:"+self.config_file)
            # инициируем логер
            logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = int(self.config['DEFAULT']['log_level']), filename = self.config['DEFAULT']['log_file'])
            logging.info (u'Logging is init.....' )
        
        def init_database(self):
            self.database=db.DB()
            self.database.set_shema_dir(self.config['ORM']['shema_files'])
            flag_debug=True
            if self.config['ORM']['debug']=="False":
                flag_debug=False
            self.database.initDataBaseEngine(self.config['DATABASE']['host'],self.config['DATABASE']['driver'],self.config['DATABASE']['database'],self.config['DATABASE']['login'],self.config['DATABASE']['password'],flag_debug)
            logging.info (u'database is init.....' )


        def log_info(self,str):
            logging.info (str)
        def log_debug(self,str):
            logging.debug (str)



    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Init.instance:
            Init.instance = Init.__Init()
        return Init.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

