from flask import Flask
from Lifewillbefun.utils.util import get_user_id

app = Flask('Lifewillbefun')
app.config.from_pyfile('app_config.cfg')
app.jinja_env.globals.update(static='/static')
app.jinja_env.globals.update(get_user_id=get_user_id)

from Lifewillbefun.views import register
