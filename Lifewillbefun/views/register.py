from Lifewillbefun import app
from flask import Flask, url_for, request, render_template, flash, make_response, redirect, escape, session
from Lifewillbefun.utils import mail

@app.route('/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        return redirect(url_for('register'))
    else:
        return render_template('regist.html')
    return render_template('regist.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        mail.sendMail(email)
        return render_template('password.html')





