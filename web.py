#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 17:19:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from app import create_app, db
from app.models import User, Post
from flask.ext.script import Manager, Shell

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
