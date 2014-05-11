# -*- coding: utf8 -*-

import smtplib, os, re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Lifewillbefun.app_config import MAIL_HOST, MAIL_USER, MAIL_PASS, MAIL_PORT
from Lifewillbefun import app

BASE_DIR = os.path.dirname(__file__)

def sendMail(mailto, code):
    me = MAIL_USER + '<' + MAIL_USER + '@' + MAIL_USER.split('@')[1] + '>'
    msg = MIMEMultipart('alternative')
    url = 'http://192.168.10.250:8000/active?' + 'email=' + mailto + '&' + 'code=' + code
    html = open(os.path.join(BASE_DIR, 'regist_mail.tpl')).read().format(url)
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
    msg['Subject'] = u"欢迎注册lifewillbefun"
    msg['From'] = me 
    msg['To'] = ''.join(mailto) 
    try:
        s = smtplib.SMTP(MAIL_HOST)
        s.login(MAIL_USER, MAIL_PASS)
        s.sendmail(me, mailto, msg.as_string())
        s.quit()
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    sendMail(mailto, code)

