# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.cache import Cache
from Lifewillbefun.utils.util import get_user_id

app = Flask('Lifewillbefun')
app.config.from_object('Lifewillbefun.app_config')
app.jinja_env.globals.update(static = '/static')
app.jinja_env.globals.update(get_user_id = get_user_id)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = u'请先登录'
cache = Cache(app, config = {'CACHE_TYPE':'simple'})

import views
