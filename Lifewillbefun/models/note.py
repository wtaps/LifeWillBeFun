from Lifewillbefun import db
from sqlalchemy import desc

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
    
    @classmethod
    def create(cls, user_id, content, time):
        note = Note(user_id, content, time)
        db.session.add(note)
        db.session.commit()
        return note

    @classmethod
    def all(cls, user_id):
        return Note.query.filter_by(user_id = user_id).order_by(desc(Note.time)).all()

    @classmethod
    def latest(cls, user_id):
        return Note.query.filter_by(user_id = user_id).order_by(desc(Note.time)).first()

    @classmethod
    def datelist(cls, user_id):
        datelist = Note.query.filter_by(user_id = user_id).order_by(desc(Note.time)).values(Note.time)
        return set(map(lambda x: x.time.strftime('%Y-%m-%d'), datelist))

    @classmethod
    def datenotes(cls, user_id, index):
        return Note.query.filter(Note.user_id == user_id).filter(Note.time.like(index)).order_by(desc(Note.time)).all()

    @classmethod
    def get_newer_note(cls, user_id, note_id):
        return Note.query.filter(Note.user_id == user_id).filter(Note.id > note_id).first()

    @classmethod
    def get_older_note(cls, user_id, note_id):
        return Note.query.filter(Note.user_id == user_id).filter(Note.id < note_id).order_by(desc(Note.id)).first()

    def __repr__(self):
        return '<Content %s>' % self.content[:20]
