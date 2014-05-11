# -*- coding: utf-8 -*-

from Lifewillbefun import app
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
import hashlib

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        email_is_existed = User.query.filter_by(email = email).first()
        if not email_is_existed:
            flash(u'用户未注册')
            return redirect(url_for('register'))
        real_email = email_is_existed.email
        salt = email_is_existed.salt
        real_password = email_is_existed.password
        if email == real_email and real_password == hashlib.md5(salt + password).hexdigest():
            session['id'] = email_is_existed.id
            return redirect(url_for('note_list'))
        flash(u'邮箱密码不正确')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('id', None)
    return redirect(url_for('login'))

