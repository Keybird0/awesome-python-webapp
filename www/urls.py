#!/usr/bin/env python
# coding: utf-8

__author__ = 'Keybird'

import os, re, time, base64, hashlib, logging
from transwarp.web import get, view, post, ctx, interceptor, seeother, notfound

from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    user = User.find_first('where email=?', 'admin@example.com')
    return dict(blogs=blogs, user=user)
