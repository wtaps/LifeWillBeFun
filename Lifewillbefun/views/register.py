# -*- coding:utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.utils import mail, util
from Lifewillbefun.models.user import User, User_regist

@app.route('/', methods=['GET', 'POST'])
def regist():
     return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip()
        email_is_existed = User_regist.query.filter_by(email = email).first()
        code = util.makeCode()
        if not email_is_existed:
            user = User_regist(email, code)
            db.session.add(user)
            db.session.commit()
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
        local_email, local_code = user_regist_mail_is_existed.email, user_regist_mail_is_existed.code
        if email == local_email and code == local_code:
            set_status = User.query.filter_by(email = email)
            set_status.update({'status':'active'})
            set_status.session.commit()
            return redirect(url_for('login')) 
    return redirect(url_for('register')) 
        

@app.route('/init-password', methods=['GET', 'POST'])
def init_password():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        salt, real_password = util.md5Password(password)
        user = User(email, real_password, email, salt, 'normal')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('password.html')
    return render_template('password.html')





