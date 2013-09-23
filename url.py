#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
from tornado.web import StaticFileHandler

from odor_handler.helloworldhandler import HelloWorldHandler
from odor_handler.authhandler import AuthHandler

urlpatterns = [
    (r"^/auth/?(.*)$", AuthHandler),
    (r"^/(favicon\.ico)$", StaticFileHandler, {"path": "static"}),
    (r"^/(robots\.txt)$", StaticFileHandler, {"path": "static"}),
    (r"^/static/(.*)$", StaticFileHandler, {"path": "static"}),
    (r"^/", HelloWorldHandler),
    ]