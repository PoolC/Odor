#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
from sqlalchemy import Column, String, Integer

from odor_model import Base

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    
    def set_password(self, clear_password):
        pass
    
    def compare_password(self, clear_password):
        pass
    
    def __init__(self, username, clear_password):
        self.username = username
        self.set_password(clear_password)
    
    def __repr__(self):
        return "<User({}, {})>".format(self.uid.__repr__(), self.username.__repr__())

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())