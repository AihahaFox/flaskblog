#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 17:12:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class PostForm(Form):
    title = StringField(u'标题', validators=[Length(1, 128), Required()])
    content = PageDownField(u'内容', validators=[Required()])
    submit = SubmitField(u'提交')
