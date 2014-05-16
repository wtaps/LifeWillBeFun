# -*- coding:utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note
import datetime

@app.route('/note-list', methods=['GET', 'POST'])
def note_list():
    notes = Note.all()
    if not notes:
        return render_template('no_note.html')
    return render_template('note_list.html', notes = notes)

@app.route('/write', methods=['GET', 'POST'])
def note_write():
    if 'id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        user_id = session['id']
        time = datetime.datetime.now()
        content = request.form['note_content']
        note = Note.create(user_id, content, time)
        return redirect(url_for('note_latest'))
    return render_template('write.html')

@app.route('/latest', methods=['GET', 'POST'])
def note_latest():
    notes = Note.all()
    return render_template('note.html', notes = notes)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    notes = Note.all()
    return render_template('note.html', notes = notes)

