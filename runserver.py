#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
from tornado.ioloop import IOLoop
from tornado.web import Application

from url import urlpatterns
from config import COOKIE_SECRET
from odor_helper.redishelper import RedisHelper
from odor_helper.session import RedisSessionStore

application_settings = {
    "cookie_secret": COOKIE_SECRET,
    }

application = Application(urlpatterns, **application_settings)
application.session_store = RedisSessionStore(RedisHelper.connection)

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()