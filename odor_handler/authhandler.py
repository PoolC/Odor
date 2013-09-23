#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 16.

@author: tintypemolly
'''
from odor_handler.basehandler import BaseHandler
from odor_helper.oauth import OdorAuthorizationProvider
from odor_helper.sqlalchemyhelper import SqlAlchemyHelper

class AuthHandler(BaseHandler):
    
    def render_get(self, path):
        if path[0] == "authorize":
            self.render_login_page()
        else:
            self.render("index.html")
    
    def render_post(self, path):
        if path[0] == "authorize":
            self.authorization_process()
    
    def render_login_page(self):
        pass
    
    def authorization_process(self):
        """
        path : auth/authorize
            description :
                login page
            http get arguments:
                client_id:          required, application id, which maps to Application.uid
                redirect_uri:       required, url-encoded uri to redirect after authorization
                response_type:      required, fixed value, "code"
                state:              optional, argument for CSRF prevention
                                    passed to client server as http get argument with same value
                display:            optional, "mobile" or "default"
            example input:
                minimum:
                    https://www.foo.com/auth/authorize?client_id=12345678&redirect_uri=https%3A%2F%2Fwww.bar.com%2Foauth%2Fcallback&response_type=code
                with argument "state":
                    https://www.foo.com/auth/authorize?client_id=12345678&redirect_uri=https%3A%2F%2Fwww.bar.com%2Foauth%2Fcallback&response_type=code&state=4f2912363b0b45bcf8acb4090b73a192
                full:
                    https://www.foo.com/auth/authorize?client_id=12345678&redirect_uri=https%3A%2F%2Fwww.bar.com%2Foauth%2Fcallback&response_type=code&state=4f2912363b0b45bcf8acb4090b73a192&display=mobile
            example return:
                minimum:
                    https://www.bar.com/oauth/callback?code=635a8e8ec74f586be353eae3ff400676
                with argument "state":
                    https://www.bar.com/oauth/callback?code=635a8e8ec74f586be353eae3ff400676&state=4f2912363b0b45bcf8acb4090b73a192
                full:
                    https://www.bar.com/oauth/callback?code=635a8e8ec74f586be353eae3ff400676&state=4f2912363b0b45bcf8acb4090b73a192
        """
        dbsession = SqlAlchemyHelper.session()
        login_user = self.get_login_user(dbsession)
        if login_user:
            response = OdorAuthorizationProvider(self).get_authorization_code_from_uri(self, self.request.uri)
            self.wrtie(response.text)
            self.set_status(response.status_code)
        else:
            self.render("login.html")