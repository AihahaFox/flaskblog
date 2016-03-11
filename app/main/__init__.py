#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 07:49:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
