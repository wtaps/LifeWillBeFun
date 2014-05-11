# -*- coding: utf-8 -*-

import random, hashlib
from flask import Flask, session

def get_user_id():
    if 'id' in session:
        return session['id']
    return 0

def makeCode():
    code = ''.join(random.sample('rvSasdwdfgSKW423JDkdsf9234adkkefhkji329skKJFEfl23asd3kdfNhfdkej34hjDSFhjhfsdfasd348HJKDSR', 20))
    return code

def md5Password(password):
    salt = ''.join(random.sample('SK32sad9(@#@kjsjfskjLKFEHFDLKJJWDLKADHEFJ3skdl3i2DS(@$&*sf723748KFDSJHdkjfd#$#$@dskjlf*%#', 10))
    hash = hashlib.md5(salt + password).hexdigest()
    return salt, hash


