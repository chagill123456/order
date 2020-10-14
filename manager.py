#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:lj
from application import app,manager
from flask_script import Server
import www

manager.add_command("runserver",Server(host='0.0.0.0',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))

def main():
    manager.run()


if __name__=='__main__':
    try:
        import sys
        sys.exit(main())
        pass
    except Exception as e:
        import traceback
        traceback.print_exc()