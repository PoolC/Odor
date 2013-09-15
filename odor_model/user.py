#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
import hashlib
import json

from sqlalchemy import Column, String, Integer

from odor_helper.security import get_hasher
from odor_helper.security.pbkdf2_hasher import PBKDF2Hasher
from odor_model import Base


class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    realname = Column(String(255), index=True)
    
    def json(self):
        # TODO json data definition
        data = {
            "username": self.username,
            "realname": self.realname,
            }
        return json.dumps(data)
    
    def set_password(self, clear_password):
        self.password = PBKDF2Hasher.derive_password_data(clear_password)
    
    def compare_password(self, clear_password):
        hasher_name = self.password.split(u"$")[0]
        hasher = get_hasher(hasher_name)
        return hasher.compare_password(self.password, clear_password)
    
    def __init__(self, username=None):
        if username:
            self.username = username
    
    def __repr__(self):
        return "<User({}, {})>".format(self.uid.__repr__(), self.username.__repr__())

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())