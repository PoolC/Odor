'''
Created on 2013. 9. 13.

@author: tintypemolly
'''
class BaseHasher(object):
    
    @staticmethod
    def generate_password_data(clear_password):
        raise NotImplementedError()
    
    @staticmethod
    def compare_password(password_data, clear_password):
        raise NotImplementedError()