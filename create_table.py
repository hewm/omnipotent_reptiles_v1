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

from omnipotent_reptiles_v1 import db, create_app

app = create_app()
app_ctx = app.app_context()  # caa_ctx = app/g
with app_ctx:  # __enter__,通过LocalStack放入Local中
    db.create_all()  # 调用LocalStack放入Local中获取app，再去app中获取配置
