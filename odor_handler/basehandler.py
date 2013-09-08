#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

@author: tintypemolly
'''
import traceback
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time

from tornado.web import RequestHandler

from odor_exception.odorexception import OdorException, internal_server_error
from odor_helper.session import Session

class BaseHandler(RequestHandler):
    
    @property
    def session(self):
        sessionid = self.get_secure_cookie('sid')
        return Session(sessionid)
    
    def get(self, raw_path=""):
        self._odor_process_request(self.render_get, "GET", raw_path)
    
    def post(self, raw_path=""):
        self._odor_process_request(self.render_post, "POST", raw_path)
    
    def render_get(self, path):
        raise NotImplementedError()
    
    def render_post(self, path):
        raise NotImplementedError()
    
    def _odor_process_request(self, function, method, raw_path):
        path = raw_path.split("/")
        if path[0]:
            path.append("")
        try:
            function(path)
        except OdorException as e:
            #echo error message to server console
            error_log_data = BaseHandler._odor_build_error_log_data(method, path)
            print "\n".join(error_log_data)
            
            #send exception response to user
            self._odor_send_exception_response(e)
        except:
            #echo error message to server console
            error_log_data = BaseHandler._odor_build_error_log_data(method, path)
            print "\n".join(error_log_data)
            
            #send exception response to user
            self._odor_send_exception_response(internal_server_error)
    
    def _odor_send_exception_response(self, e):
        self._write_buffer = []
        error_data = {}
        error_data["errno"] = e.odor_internal_errno
        if e.message:
            error_data["message"] = e.message
        self.set_status(e.http_status_code)
        self.write(error_data)
    
    @staticmethod
    def _odor_build_error_log_data(method, path):
        timestamp = mktime(datetime.now().timetuple())
        time_str = format_date_time(timestamp)
        stack_trace = traceback.format_exc()
        error_log_data = [
            time_str,
            method,
            "/".join(path),
            stack_trace,
            ]
        return error_log_data