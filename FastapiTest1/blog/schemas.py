from ctypes.wintypes import FLOAT
from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):

    SocketNumber: Optional[int]=None 
    MachineName: Optional[str]=None 
    System_Name: Optional[str]=None 
    TotalRam: Optional[int]=None 
    FreeRam: Optional[int]=None 
    RamUsage: Optional[int]=None 
    System_Idle_Window : Optional[int]=None 
    Date_and_Time : Optional[str]=None 
    Cpu_Usage : Optional[float]=None 
    TotalDiskSpace : Optional[int]=None 
    FreeDiskSpace : Optional[int]=None 
    ErrorMessage : Optional[str]=None 

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):

    SocketNumber: Optional[int]=None 
    MachineName: Optional[str]=None 
    System_Name: Optional[str]=None 
    TotalRam: Optional[int]=None 
    FreeRam: Optional[int]=None 
    RamUsage: Optional[int]=None 
    System_Idle_Window : Optional[int]=None 
    Date_and_Time : Optional[str]=None 
    Cpu_Usage : Optional[float]=None 
    TotalDiskSpace : Optional[int]=None 
    FreeDiskSpace : Optional[int]=None 
    ErrorMessage : Optional[str]=None 

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
