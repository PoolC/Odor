#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
from odor_handler.helloworldhandler import HelloWorldHandler
from tornado.web import StaticFileHandler

urlpatterns = [
    (r"^/(favicon\.ico)$", StaticFileHandler, {"path": "static"}),
    (r"^/", HelloWorldHandler),
    ]