"""
创建时间 : 2018/07/02
版本号 : V1
文档名 : account.py
编辑人 : he_wm
作 用 : 用户登录相关
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
ac = Blueprint('ac', __name__)


@ac.route('/login')
def login():
    return 'login'


@ac.route('/logout')
def logout():
    return 'logout'
