#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 13.

@author: tintypemolly
'''
import os

from Crypto.Hash import HMAC, SHA256
from pbkdf2 import PBKDF2

class PBKDF2Hasher(object):
    
    iteration = 1000
    digestmodule = SHA256
    macmodule = HMAC
    
    @staticmethod
    def generate_password_data(clear_password):
        salt = PBKDF2Hasher._generate_salt()
        key = PBKDF2(clear_password,
                     salt,
                     PBKDF2Hasher.iteration,
                     PBKDF2Hasher.digestmodule,
                     PBKDF2Hasher.macmodule)
        hash_value = key.read(32)
        data = [
            u"pbkdf2",
            salt,
            unicode(PBKDF2Hasher.iteration),
            unicode(hash_value),
            ]
        return u"$".join(data) 
    
    @staticmethod
    def _generate_salt():
        raw_salt = os.urandom(16)
        salt = u""
        for character in raw_salt:
            salt += u"%02x" % ord(character)
        return salt

for i in range(10): print PBKDF2Hasher._generate_salt()