'''
Created on 2013. 9. 16.

@author: tintypemolly
'''
import hashlib

from odor_helper.security.basehasher import BaseHasher

class MD5Hasher(BaseHasher):
    hasher_name = u"md5"
    
    @staticmethod
    def derive_password_data(clear_password):
        data = [
            MD5Hasher.hasher_name,
            unicode(hashlib.md5(clear_password).hexdigest())
            ]
        return u"$".join(data)
    
    @staticmethod
    def compare_password(derived_password_data, clear_password):
        hasher_name, hash_value = derived_password_data.split(u"$")
        if hasher_name != MD5Hasher.hasher_name:
            raise ValueError("hasher name of derived password data is not md5")
        return hash_value == unicode(hashlib.md5(clear_password).hexdigest())
