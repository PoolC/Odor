#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
from tornado.ioloop import IOLoop
from tornado.web import Application

from url import urlpatterns
from config import COOKIE_SECRET

application_settings = {
    "cookie_secret": COOKIE_SECRET,
    "xsrf_cookies": True,
    "template_path": "template"
    }

application = Application(urlpatterns, **application_settings)

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()