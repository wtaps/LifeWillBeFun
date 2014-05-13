# -*- coding:utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.utils import mail, util
from Lifewillbefun.models.user import User, User_regist

@app.route('/')
def regist():
     return render_template('regist.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip()
        email_is_valid = mail.checkEmail(email)
        if not email_is_valid:
            flash(u'请输入合法的邮箱')
            return render_template('regist.html')
        email_is_existed = User_regist.query.filter_by(email = email).first()
        code = util.makeCode()
        if not email_is_existed:
            User_regist.create(email, code)
            mail.sendMail(email, code)
            return render_template('password.html', email = email)
        else:
            flash(u'此邮箱已经注册')
    return render_template('regist.html')

@app.route('/active')
def active():
    email = request.args.get('email')
    code = request.args.get('code')
    user_email_is_existed = User.query.filter_by(email = email).first()
    if not user_email_is_existed:
        flash(u'此邮箱还未设置密码，请设置密码')
        return render_template('password.html', email = email)
    else:
        user_regist_mail_is_existed = User_regist.query.filter_by(email = email).first()
        if user_regist_mail_is_existed.checkCode(code):
            user_email_is_existed.setStatus('active')
            return redirect(url_for('login')) 
    return redirect(url_for('register')) 
        

@app.route('/init-password', methods=['GET', 'POST'])
def init_password():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        salt, real_password = util.md5Password(password)
        user = User.create(email, real_password, email, salt)
        session['id'] = user.id
        return redirect(url_for('login'))
    return render_template('password.html')

