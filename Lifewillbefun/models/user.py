from Lifewillbefun import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(120))
    email = db.Column(db.String(63), unique=True)
    salt = db.Column(db.String(30))
    create_time = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    def __init__(self, username, password, email, salt, status):
        self.username = username
        self.password = password
        self.email = email
        self.salt = salt
        self.status = status

    def __repr__(self):
        return '<User %r>' % self.username


class User_regist(db.Model):
    __tablename__ = 'user_regist'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(63), unique=True, default='')
    code = db.Column(db.String(150), default='')
    create_time = db.Column(db.DateTime)
    
    def __init__(self, email, code):
        self.email = email
        self.code = code

    def __repr__(self):
        return '<Email %r>' % self.email



