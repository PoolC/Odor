#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: Marco
'''
from tornado.ioloop import IOLoop
from tornado.web import Application

from url import urlpatterns

application = Application(urlpatterns)

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()