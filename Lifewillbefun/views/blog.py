# -*- coding: utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note
import datetime

@app.route('/note-list', methods=['GET', 'POST'])
def note_list():
    if 'id' not in session:
        return redirect(url_for('login'))
    notes = Note.all(session['id'])
    date_list = set(map(lambda x: x.time.strftime('%Y-%m-%d'), Note.datelist(session['id'])))
    if not notes:
        return render_template('no_notes.html')
    return render_template('note_list.html', notes = notes, date_list = date_list)

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
    if 'id' not in session:
        return redirect(url_for('login'))
    note = Note.latest(session['id'])
    return render_template('note.html', note = note)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'id' not in session:
        return redirect(url_for('login'))
    notes = Note.all(session['id'])
    return render_template('note.html', notes = notes)

@app.route('/notes/<date>', methods=['GET', 'POST'])
def notes_date(date):
    if 'id' not in session:
        return redirect(url_for('login'))
    index = '{0}%'.format(date)
    notes = Note.datenotes(session['id'], index)
    return render_template('note.html', notes = notes)



