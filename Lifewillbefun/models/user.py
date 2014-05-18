from Lifewillbefun import db
import hashlib

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

    @classmethod
    def create(cls, username, password, email, salt, status):
        user = User(username, password, email, salt, status)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def query_by_email(cls, email):
        return User.query.filter_by(email = email).first()

    @classmethod
    def query_by_id(cls, id):
        return User.query.filter_by(id = id).first()

    def setStatus(self, status):
        self.status = status
        db.session.commit()

    def changePassword(self, password):
        self.password = hashlib.md5(self.salt + password).hexdigest()
        db.session.commit()

    def checkPassword(self, password):
        return self.password == hashlib.md5(self.salt + password).hexdigest()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
        
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

    @classmethod
    def create(cls, email, code):
        user = User_regist(email, code)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def query_by_email(cls, email):
        return User_regist.query.filter_by(email = email).first()

    def checkCode(self, code):
        return self.code == code

    def __repr__(self):
        return '<Email %r>' % self.email
