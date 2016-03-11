#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 17:04:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
