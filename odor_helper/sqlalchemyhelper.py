#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
from sqlalchemy import create_engine
from config import (
    DEBUG,
    MYSQL_DATABSE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_USERNAME
    )

class SqlAlchemyHelper(object):
    _connection_data = [
        "mysql://",
        MYSQL_USERNAME,
        ":",
        MYSQL_PASSWORD,
        "@",
        MYSQL_HOST,
        "/",
        MYSQL_DATABSE,
        "?charset=utf-8",
        ]
    _connection_string = "".join(_connection_data)
    print _connection_string
    engine = create_engine(_connection_string, echo=DEBUG)
    
    def __init__(self):
        pass

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())