#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 5.

This is base class of all handled exception within the odor server.

@author: tintypemolly
'''
class OdorException(Exception):
    
    def __init__(self, http_status_code, odor_internal_errno, message=None):
        self.http_status_code = http_status_code
        self.odor_internal_errno = odor_internal_errno
        self.message = message

internal_server_error = OdorException(500, 10000, "Internal Server Error")