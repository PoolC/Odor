#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 13.

@author: tintypemolly
'''
import base64
import os

from Crypto.Hash import HMAC, SHA256
from pbkdf2 import PBKDF2

from odor_helper.security.basehasher import BaseHasher

class PBKDF2Hasher(BaseHasher):
    hasher_name = u"pbkdf2"
    iteration = 1000
    digestmodule = SHA256
    macmodule = HMAC
    
    @staticmethod
    def derive_password_data(clear_password):
        salt = os.urandom(16)
        key = PBKDF2(clear_password,
                     salt,
                     PBKDF2Hasher.iteration,
                     PBKDF2Hasher.digestmodule,
                     PBKDF2Hasher.macmodule)
        derived_key = key.read(32)
        data = [
            PBKDF2Hasher.hasher_name,
            unicode(base64.b64encode(salt)),
            unicode(PBKDF2Hasher.iteration),
            unicode(base64.b64encode(derived_key)),
            ]
        return u"$".join(data)
    
    @staticmethod
    def compare_password(derived_password_data, clear_password):
        hasher_name, salt, iteration, hash_value = derived_password_data.split(u"$")
        if hasher_name != PBKDF2Hasher.hasher_name:
            raise ValueError("hasher name of derived password data is not pbkdf2")
        iteration = int(iteration)
        raw_salt = base64.b64decode(salt)
        key = PBKDF2(clear_password,
                     raw_salt,
                     iteration,
                     PBKDF2Hasher.digestmodule,
                     PBKDF2Hasher.macmodule)
        return hash_value == base64.b64encode(key.read(32))
