# -*- coding: utf-8 -*-

from Lifewillbefun.utils.mail import checkEmail
from Lifewillbefun.models.user import User, User_regist

class FormMessage(object):
    def __init__(self, is_success, message = ''):
        self.is_success = is_success
        self.message = message

class RegistForm(object):
    def __init__(self, email):
        self.email = email

    def validate(self):
        if self.email == '':
            return FormMessage(False, u'邮件不能为空')
        if not checkEmail(self.email):
            return FormMessage(False, u'请输入合法的邮件地址')
        return FormMessage(True)
