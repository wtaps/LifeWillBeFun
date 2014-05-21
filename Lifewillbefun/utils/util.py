# -*- coding: utf-8 -*-

import random, hashlib
from flask.ext.login import current_user

def get_user_id():
    if hasattr(current_user, 'id'):
        return current_user.id
    return 0

def makeCode():
    code = ''.join(random.sample('rvSasdwdfgSKW423JDkdsf9234adkkefhkji329skKJFEfl23asd3kdfNhfdkej34hjDSFhjhfsdfasd348HJKDSR', 20))
    return code

def md5Password(password):
    salt = ''.join(random.sample('SK32sad9(@#@kjsjfskjLKFEHFDLKJJWDLKADHEFJ3skdl3i2DS(@$&*sf723748KFDSJHdkjfd#$#$@dskjlf*%#', 10))
    hash = hashlib.md5(salt + password).hexdigest()
    return salt, hash

def get_local_date(time):
    return time.strftime('%Y年%m月%d日').decode('utf8')

def get_local_weekday(time):
    weekday_dict = {0:'一', 
                    1:'二',    
                    2:'三',   
                    3:'四',   
                    4:'五',   
                    5:'六',   
                    6:'日',   
                }
    return u'星期%s' % weekday_dict[time.weekday()].decode('utf8')


