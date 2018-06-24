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
from redis import Redis


class BaseConfig(object):
    # flask_session的相应配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='127.0.0.1', port=6379)
    # SQLAlchemy基本配置文件
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/s9?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5


class ProConfig(BaseConfig):
    pass
