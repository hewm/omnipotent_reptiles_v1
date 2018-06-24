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
from flask import Blueprint
from omnipotent_reptiles_v1 import db
from omnipotent_reptiles_v1 import models


us = Blueprint('us', __name__)


@us.route('/index')
def index():
    # db.session.add(models.Userinfo(name='123',pwd='sdad'))
    # db.session.commit()
    # db.session.remove()
    return 'index'
