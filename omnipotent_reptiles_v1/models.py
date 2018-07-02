"""
创建时间 : 2018/07/02
版本号 : V1
文档名 : models.py
编辑人 : he_wm
作 用 : 使用sqlalchemy创建数据库映射
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
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, Date, DateTime

from omnipotent_reptiles_v1 import db


class Userinfo(db.Model):
    __tablename__ = 'userinfo'
    id = Column(Integer, primary_key=True)
    user = Column(String(32), index=True, nullable=False)
    pwd = Column(String(32), index=True, nullable=False)
