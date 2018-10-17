#!/usr/bin/python
## -*- coding: utf-8 -*-
import bcrypt


def encrypt(value):
    string = "UA4VaxURJ0PCLXBh"
    value = str(value) + str(string)
    value = value.encode('utf8')
    hashed = bcrypt.hashpw(value, bcrypt.gensalt())
    return hashed

def confirm(value, hashed):
    string = "UA4VaxURJ0PCLXBh"
    value = str(value) + str(string)
    value = value.encode('utf8')
    if bcrypt.checkpw(value, hashed):
        return True
    else:
        return False
