# -*- coding: utf8 -*-

import smtplib, sys, os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Lifewillbefun import app


def sendMail(mailto):
    #me = user + '<' + user + '@' + postfix + '>'
    me = app.config['MAIL_USER']
    msg = MIMEMultipart('alternative')
    html = open(os.path.join(os.getcwd(), 'Lifewillbefun/utils/regist_mail.tpl')).read()
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
    #msg = MIMEText(u"注册", _subtype='html', _charset='gbk') 
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

