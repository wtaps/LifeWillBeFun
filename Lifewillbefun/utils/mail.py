# -*- coding: utf8 -*-

import smtplib, sys, os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Lifewillbefun import app

BASE_DIR = os.path.dirname(__file__)


def sendMail(mailto):
    #me = user + '<' + user + '@' + postfix + '>'
    me = app.config['MAIL_USER']
    msg = MIMEMultipart('alternative')
    html = open(os.path.join(BASE_DIR, 'regist_mail.tpl')).read()
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
    msg['Subject'] = u"Welcome to regist"
    msg['From'] = me 
    msg['To'] = ''.join(mailto) 

    try:
        s = smtplib.SMTP(app.config['MAIL_HOST'])
        s.login(app.config['MAIL_USER'], app.config['MAIL_PASS'])
        s.sendmail(me, mailto, msg.as_string())
        s.quit()
    except:
        print 'mail fault'

if __name__ == '__main__':
    sendMail(mailto)

