# -*- coding:utf-8 -*-

from Lifewillbefun import app, db
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.models.user import User, User_regist
from Lifewillbefun.models.note import Note
from flask.ext.login import login_required, current_user


@app.route('/setting/password', methods=['GET', 'POST'])
@login_required
def settings():
    #if 'id' not in session:
    #    flash(u'请先登陆')
    #    return redirect(url_for('login'))
    if request.method == 'POST':
        user = User.query_by_id(current_user.id)
        old = request.form['old'].strip()
        new = request.form['new'].strip()
        confirm = request.form['confirm'].strip()
        if not user.checkPassword(old):
            flash(u'原密码不正确')
            return render_template('change_password.html')
        if new != confirm:
            flash(u'两次密码输入不一致')
            return render_template('change_password.html')
        result = user.changePassword(new)
        if result:
            flash(u'密码修改成功')
            return redirect(url_for('login'))
        else:
            flash(u'密码修改失败，请重新修改')
    return render_template('change_password.html')

