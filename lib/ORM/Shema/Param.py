from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import Table, MetaData

Base=declarative_base()

class Param(Base):
    __tablename__ = 'params'
    device_id = Column(Integer)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    type = Column(String)
    isWrite = Column(Enum('Y','N'))
    isAdd = Column(Enum('Y','N'))
    add_path = Column(String)
    tr69_interface = Column(String)
    

