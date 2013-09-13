#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
from odor_handler.basehandler import BaseHandler

class HelloWorldHandler(BaseHandler):
    def render_get(self, path):
        self.write("Hello, World!")
