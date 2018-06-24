"""
创建时间 : 
版本号 : V
文档名 : 
编辑人 : he_wm
作 用 : 
源存储位置 : 
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Date, DateTime
from sqlalchemy import create_engine
from omnipotent_reptiles_v1 import db


class Userinfo(db.Model):
    __tablename__ = 'userinfo'
    id = Column(Integer, primary_key=True)
    user = Column(String(32), index=True, nullable=False)
    pwd = Column(String(32), index=True, nullable=False)
