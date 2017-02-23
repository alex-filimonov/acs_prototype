from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import Table, MetaData

Base=declarative_base()

class ParamDefault(Base):
    __tablename__ = 'params_default'
    device_id = Column(Integer)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    isWrite = Column(Enum('Y','N'))
    type = Column(String)
    tr69_interface = Column(String)
    
    

