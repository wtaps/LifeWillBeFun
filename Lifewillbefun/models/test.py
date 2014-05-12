from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:111@127.0.0.1/flask?charset=utf8'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
#    code = db.Column(db.String(100))

    def __init__(self, username, email):
        self.username = username
        self.email = email
#        self.code = code

    def __repr__(self):
        return '%r,%r' % (self.username, self.email)
class Userinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    address = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('userinfos', lazy='dynamic'))

    def __init__(self, phone, address, user):
        self.phone = phone
        self.address = address
        self.user = user

    def __repr__(self):
        return '<Userinfo %r>' % self.phone
db.create_all()

