#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 13.

@author: tintypemolly
'''
class BaseHasher(object):
    
    @staticmethod
    def derive_password_data(clear_password):
        raise NotImplementedError()
    
    @staticmethod
    def compare_password(derived_password_data, clear_password):
        raise NotImplementedError()