"""
创建时间 : 2018/06/24
版本号 : V1
文档名 : __init__.py
编辑人 : he_wm
作 用 : 
源存储位置 : \\omnipotent_reptiles_v1\\__init__.py
"""
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# 导入并实例化一个SQLAlchemy对象
db = SQLAlchemy()

from .models import *
from .views.user import us
from .views.account import ac


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.BaseConfig')
    app.register_blueprint(ac)
    app.register_blueprint(us)
    # flask_session:第一步实例化Session
    Session(app)
    db.init_app(app)

    return app
