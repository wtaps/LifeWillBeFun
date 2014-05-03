from flask import Flask
app = Flask('Lifewillbefun')
app.config.from_pyfile('app_config.cfg')

from Lifewillbefun.views import regist
