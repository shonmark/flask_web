#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : manage.py
# @Author: shone
# @Date  : 2017/11/5
from flask_script import Manager, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=5000, use_debugger=True))


@manager.command
def dev():
    print('hello')


if __name__ == '__main__':
    manager.run()
