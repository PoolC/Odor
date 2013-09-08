#-*- coding: utf-8 -*-
'''
Created on 2013. 9. 7.

@author: tintypemolly
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    connection_string = "".join(_connection_data)
    engine = create_engine(connection_string, echo=DEBUG)
    _Session = sessionmaker(bind=engine)
    
    @classmethod
    def engine(cls):
        return cls.engine
    
    @classmethod
    def session(cls):
        return cls._Session()

if __name__ == "__main__":
    import code
    code.interact(None, None, locals())