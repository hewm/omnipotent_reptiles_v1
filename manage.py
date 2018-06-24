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
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from omnipotent_reptiles_v1 import db
from omnipotent_reptiles_v1 import create_app

app = create_app()
manager = Manager(app)
Migrate(app, db)
"""
数据库迁移命令
    python manage.py db init
    python manage.py db migrate  # makemirations
    python manage.py db upgrade  # migrate
"""
manager.add_command('db', MigrateCommand)


@manager.command
def custom(arg):
    """
    自定义命令
    Python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)


if __name__ == "__main__":
    manager.run()
