#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 07:36:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app