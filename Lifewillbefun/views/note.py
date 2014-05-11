# -*- coding:utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note

@app.route('/note-list', methods=['GET', 'POST'])
def note_list():
    return render_template('note_list.html')

@app.route('/write', methods=['GET', 'POST'])
def note_write():
    if 'id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        user_id = session['id']
        time = request.form['note_date']
        content = request.form['note_content']
        note = Note(user_id, content, time)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('note_latest'))
    return render_template('write.html')

@app.route('/latest', methods=['GET', 'POST'])
def note_latest():
    entities = Note.query.order_by(Note.time.desc()).limit(3).all()
    return str(entities)


