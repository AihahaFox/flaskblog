#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-14 17:05:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import admin
from .. import db
from ..models import User, Post
from .forms import LoginForm, PostForm


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.index'))
        flash('Invalid username or password')
    return render_template('admin/login.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/new-post', methods=['GET', 'POST'])
@login_required
def newpost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        return redirect(url_for('main.index'))
    return render_template('admin/edit_post.html', form=form)


@admin.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def editpost(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.add(post)
        flash('This post has been updated.')
        return redirect(url_for('post', id=post.id))
    return render_template('admin/edit_post.html', form=form)
