from pickle import FLOAT
from pickletools import float8
from tkinter.tix import COLUMN
from sqlalchemy import Column, Integer, String,Float
from blog.database import Base
from . import schemas


class Blog(Base):
    __tablename__ = 'FinalTable'

    id = Column(Integer, primary_key=True, index=True)
    SocketNumber = Column(Integer)
    MachineName = Column(String(32))
    System_Name=Column(String(64))
    TotalRam=Column(Integer)
    FreeRam=Column(Integer)
    RamUsage=Column(Integer)
    System_Idle_Window=Column(Integer)
    Date_and_Time=Column(String(128))
    Cpu_Usage=Column(Float)
    TotalDiskSpace=Column(Integer)
    FreeDiskSpace=Column(Integer)
    ErrorMessage=Column(String(256))
    
    def __init__(self,request:schemas.Blog):

        self.SocketNumber = request.SocketNumber
        self.MachineName = request.MachineName
        self.System_Name = request.System_Name
        self.TotalRam = request.TotalRam
        self.FreeRam = request.FreeRam
        self.RamUsage = request.RamUsage
        self.System_Idle_Window = request.System_Idle_Window
        self.Date_and_Time = request.Date_and_Time
        self.Cpu_Usage = request.Cpu_Usage
        self.TotalDiskSpace = request.TotalDiskSpace
        self.FreeDiskSpace = request.FreeDiskSpace
        self.ErrorMessage = request.ErrorMessage



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16))
    email = Column(String(32))
    password = Column(String(2048))

