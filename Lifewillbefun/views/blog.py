# -*- coding: utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session, jsonify, g
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note
from Lifewillbefun.utils.util import get_local_date, get_local_weekday
from flask.ext.login import login_required, current_user
from Lifewillbefun import login_manager
import datetime, random

@login_manager.user_loader
def load_user(userid):
        return User.query.get(int(userid))

@app.route('/note-list', methods=['GET', 'POST'])
@login_required
def note_list():
    notes = Note.all(current_user.id)
    date_list = Note.datelist(current_user.id)
    if not notes:
        return render_template('no_notes.html')
    for note in notes:
        note.weekday = get_local_weekday(note.time)
        note.time = get_local_date(note.time)
    return render_template('note_list.html', notes = notes, date_list = date_list)

@app.route('/write', methods=['GET', 'POST'])
@login_required
def note_write():
    if request.method == 'POST':
        user_id = current_user.id
        time = datetime.datetime.now()
        content = request.form['note_content']
        note = Note.create(user_id, content, time)
        return redirect(url_for('note_latest'))
    return render_template('write.html')

@app.route('/latest', methods=['GET', 'POST'])
@login_required
def note_latest():
    note = Note.latest(current_user.id)
    note.weekday = get_local_weekday(note.time)
    note.time = get_local_date(note.time)
    return render_template('note.html', note = note)

@app.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    notes = Note.all(current_user.id)
    if not notes:
        return redirect(url_for('no_notes'))
    for note in notes:
        note.weekday = get_local_weekday(note.time)
        note.time = get_local_date(note.time)
    return render_template('note.html', notes = notes)

@app.route('/notes/<date>', methods=['GET', 'POST'])
@login_required
def notes_date(date):
    index = '{0}%'.format(date)
    notes = Note.datenotes(current_user.id, index)
    for note in notes:
        note.weekday = get_local_weekday(note.time)
        note.time = get_local_date(note.time)
    return render_template('note.html', notes = notes)

@app.route('/get_older_note')
@login_required
def get_older_note():
    blog_id = request.args.get('note_id')
    note = Note.get_older_note(current_user.id, blog_id)
    if not note:
        note = Note.query.filter_by(id = blog_id).first()
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(id = note_id, 
                   weekday = note_weekday,
                   time = note_time,
                   content = note_content
                )

@app.route('/get_newer_note')
@login_required
def get_newer_note():
    blog_id = request.args.get('note_id')
    note = Note.get_newer_note(current_user.id, blog_id)
    if not note:
        note = Note.query.filter_by(id = blog_id).first()
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(id = note_id, 
                   weekday = note_weekday,
                   time = note_time,
                   content = note_content
                )

@app.route('/get_random_note')
@login_required
def get_random_note():
    blog_id = request.args.get('note_id')
    notes = Note.all(current_user.id)
    if not notes:
        return redirect(url_for('no_notes'))
    note = notes[random.randint(0, len(notes) - 1)]
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(id = note_id, 
                   weekday = note_weekday,
                   time = note_time,
                   content = note_content
                )

@app.route('/no-notes')
@login_required
def no_notes():
    return render_template('no_notes.html')

