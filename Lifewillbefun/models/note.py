from Lifewillbefun import db

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, key='user_id')
    time = db.Column(db.TIMESTAMP, nullable=False)
    update_time = db.Column(db.TIMESTAMP, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, user_id, content, time):
        self.user_id = user_id
        self.content = content
        self.time = time
        self.update_time = time

    def __repr__(self):
        return '<Content %s>' % self.content[:20]
