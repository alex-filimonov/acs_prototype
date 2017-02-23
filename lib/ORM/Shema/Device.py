from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Enum
from sqlalchemy import Table, MetaData

Base=declarative_base()

class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Enum('on','off'))
    connect_request_pid = Column(String)
    def __repr__(self):
        return "<Device(name='%s')>" % (self.name)

