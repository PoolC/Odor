#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
import hashlib
import json

from pbkdf2 import PBKDF2
from sqlalchemy import Column, String, Integer

from odor_model import Base

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    realname = Column(String(255))
    
    def json(self):
        # TODO json data definition
        data = {
            "username": self.username,
            "realname": self.realname,
            }
        return json.dumps(data)
    
    def set_password(self, clear_password):
        pass
    
    def compare_password(self, clear_password):
        '''
        MD5 password field format:
        
        md5$HASH_VALUE
        
        PBKDF2 password field format:
        
        pbkdf2$SALT$ITERATION$HASH_VALUE 
        '''
        hasher = self.password.split("$")[0]
        # TODO compare password using hasher
    
    def __init__(self, username, clear_password):
        self.username = username
        self.set_password(clear_password)
    
    def __repr__(self):
        return "<User({}, {})>".format(self.uid.__repr__(), self.username.__repr__())

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())