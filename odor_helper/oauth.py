#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 8.

@author: tintypemolly
'''
import json

from pyoauth2.provider import AuthorizationProvider, ResourceProvider, ResourceAuthorization

from config import ACCESS_TOKEN_EXPIRATION_TIME
from odor_helper.redishelper import RedisHelper
from odor_model.application import Application

def authorization_code_redis_name(code):
    return 'authorization_code:%s' % code

def access_token_redis_name(access_token):
    return 'access_token:%s' % access_token

def refresh_token_redis_name(refresh_token):
    return 'refresh_token:%s' % refresh_token

class OdorAuthorizationProvider(AuthorizationProvider):
    
    def __init__(self, request_handler):
        self._request_handler = request_handler
    
    #region overridden from AuthorizationProvider
    
    @property
    def token_expires_in(self):
        return ACCESS_TOKEN_EXPIRATION_TIME
    
    def validate_client_id(self, client_id):
        dbsession = self._request_handler.dbsession
        query = dbsession.query(Application).filter(Application.uid == client_id)
        result = query.all()
        if result:
            dbsession.close()
            return True
        else:
            dbsession.close()
            return False

    def validate_client_secret(self, client_id, client_secret):
        dbsession = self._request_handler.dbsession
        query = dbsession.query(Application).filter(Application.uid == client_id)
        result = query.all()
        if not result:
            dbsession.close()
            return False
        if result:
            application = result[0]
            app_secret = application.app_secret
            dbsession.close()
            return app_secret == client_secret

    def validate_redirect_uri(self, client_id, redirect_uri):
        dbsession = self._request_handler.dbsession
        query = dbsession.query(Application).filter(Application.uid == client_id)
        result = query.all()
        if not result:
            dbsession.close()
            return False
        if result:
            application = result[0]
            app_redirect_uri = application.app_redirect_uri
            dbsession.close()
            return app_redirect_uri == redirect_uri

    def validate_scope(self, client_id, scope):
        return True

    def validate_access(self):
        dbsession = self._request_handler.dbsession
        user = self._request_handler.get_login_user(dbsession)
        validity = True if user else False
        dbsession.close()
        return validity

    def from_authorization_code(self, client_id, code, scope):
        name = authorization_code_redis_name(code)
        raw_data = RedisHelper.connection.get(name)
        return json.loads(raw_data) if raw_data else None

    def from_refresh_token(self, client_id, refresh_token, scope):
        name = refresh_token_redis_name(refresh_token)
        raw_data = RedisHelper.connection.get(name)
        return json.loads(raw_data) if raw_data else None

    def persist_authorization_code(self, client_id, code, scope):
        dbsession = self._request_handler.dbsession
        data = {
            "client_id": client_id,
            "code": code,
            "scope": scope,
            "user_id": self._request_handler.get_login_user(dbsession).uid,
            }
        dbsession.close()
        name = authorization_code_redis_name(code)
        RedisHelper.connection.set(name, json.dumps(data))

    def persist_token_information(self, client_id, scope, access_token,
                                  token_type, expires_in, refresh_token,
                                  data):
        del(data["code"])
        access_token_name = access_token_redis_name(access_token)
        refresh_token_name = refresh_token_redis_name(refresh_token)
        RedisHelper.connection.set(access_token_name, json.dumps(data))
        RedisHelper.connection.expire(access_token_name, expires_in)
        RedisHelper.connection.set(refresh_token_name, json.dumps(data))

    def discard_authorization_code(self, client_id, code):
        name = authorization_code_redis_name(code)
        RedisHelper.connection.delete(name)

    def discard_refresh_token(self, client_id, refresh_token):
        name = refresh_token_redis_name(refresh_token)
        RedisHelper.connection.delete(name)
    
    #endregion

class OdorResourceAuthorization(ResourceAuthorization):
    user_id = None

class OdorResourceProvider(ResourceProvider):
    
    def __init__(self, request_handler):
        self._request_handler = request_handler
        
    #region overridden from ResourceAuthorization
    
    @property
    def authorization_class(self):
        return OdorResourceProvider
    
    def get_authorization_header(self):
        return self._request_handler.request.headers.get("Authorization")

    def validate_access_token(self, access_token, authorization):
        name = access_token_redis_name(access_token)
        raw_data = RedisHelper.connection.get(name)
        data = json.loads(raw_data) if raw_data else None
        if data:
            authorization = OdorResourceProvider()
            authorization.is_valid = True
            authorization.token = access_token
            authorization.client_id = data.get("client_id")
            authorization.expires_in = RedisHelper.connection.ttl(name)
            authorization.user_id = data.get("user_id")
    
    #endregion