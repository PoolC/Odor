#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
import tornado
from sqlalchemy import Column, String, Integer, Text

from odor_helper.redishelper import RedisHelper
from odor_helper.session import RedisSessionStore
from odor_model import Base

class Application(Base):
    __tablename__ = "application"
    uid = Column(Integer, primary_key=True)
    app_name = Column(String(255), unique=True)
    app_secret = Column(String(255))
    app_redirect_uri = Column(Text)
    
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        self.redis = RedisHelper.connection
        self.session_store = RedisSessionStore(self.redis)
    
    def __repr__(self):
        return "<Application({}, {})>".format(self.uid.__repr__(), self.app_name.__repr__())

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())