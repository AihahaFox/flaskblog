#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 07:34:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aihahafox'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_POSTS_PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:@127.0.0.1/data-dev'


class TestinfConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://root:@127.0.0.1/data-test'


config = {
    'development': DevelopmentConfig,
    'testing': TestinfConfig,
    'default': DevelopmentConfig
}
