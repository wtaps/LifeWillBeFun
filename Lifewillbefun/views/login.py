# -*- coding: utf-8 -*-

from Lifewillbefun import app
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.utils.mail import checkEmail
from Lifewillbefun import login_manager
from flask.ext.login import login_user, logout_user, login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        email_is_valid = checkEmail(email)
        if not email_is_valid:
            flash(u'请输入合法的邮箱')
            return render_template('login.html')
        email_is_existed = User.query_by_email(email)
        if not email_is_existed:
            flash(u'用户未注册')
            return redirect(url_for('register'))
        if email_is_existed.checkPassword(password):
            flash(u'登录成功')
            login_user(email_is_existed)
            return redirect(request.args.get('next') or url_for('note_list'))
        flash(u'邮箱密码不正确')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

