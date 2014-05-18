# -*- coding: utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session, jsonify
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note
from Lifewillbefun.utils.util import get_local_date, get_local_weekday
import datetime
#from flask.ext.login import login_required
#from Lifewillbefun import login_manager
#@login_manager.user_loader
#def load_user(userid):
#        return User.query.get(userid)

@app.route('/note-list', methods=['GET', 'POST'])
def note_list():
    #if 'id' not in session:
    #    return redirect(url_for('login'))
    notes = Note.all(session['id'])
    date_list = Note.datelist(session['id'])
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

@app.route('/get_older_note')
def get_older_note():
    if 'id' not in session:
        return redirect(url_for('login'))
    blog_id = request.args.get('note_id')
    note = Note.query.filter(Note.user_id == session['id']).filter(Note.id < blog_id).order_by('-id').first()
    if not note:
        note = Note.query.filter_by(id = blog_id).first()
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(id = note_id, 
                   weekday = note_weekday,
                   time = note_time,
                   content = note_content)

@app.route('/get_newer_note')
def get_newer_note():
    if 'id' not in session:
        return redirect(url_for('login'))
    blog_id = request.args.get('note_id')
    note = Note.query.filter(Note.user_id == session['id']).filter(Note.id > blog_id).first()
    if not note:
        note = Note.query.filter_by(id = blog_id).first()
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(id = note_id, 
                   weekday = note_weekday,
                   time = note_time,
                   content = note_content)

