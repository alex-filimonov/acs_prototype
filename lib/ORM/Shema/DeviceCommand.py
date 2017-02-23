from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Enum
from sqlalchemy import Table, MetaData

Base=declarative_base()

class DeviceCommand(Base):
    __tablename__ = 'device_command'
    device_id = Column(Integer)
    id = Column(Integer, primary_key=True)
    command = Column(Enum('power_on','power_off','reboot','connect_request','factory_reset','download'))
    status = Column(Enum('wait','processing','done','error'))
    download_url = Column(String)
    
    

