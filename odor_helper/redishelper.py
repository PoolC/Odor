#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
import redis

from config import REDIS_HOST

class RedisHelper(object):
    connection = redis.StrictRedis(host=REDIS_HOST)
    
if __name__ == "__main__":
    import code
    code.interact(None, None, locals())