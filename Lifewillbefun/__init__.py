from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from Lifewillbefun.utils.util import get_user_id

app = Flask('Lifewillbefun')
app.config.from_object('Lifewillbefun.app_config')
app.jinja_env.globals.update(static = '/static')
app.jinja_env.globals.update(get_user_id = get_user_id)
db = SQLAlchemy(app)

from Lifewillbefun.views import register, login, blog
