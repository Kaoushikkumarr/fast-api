"""
This file is basically for establishing the Data Base Connection and
Credentials are taken from the .ini file.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connect import cnf_dict


def get_db_connection():

    DATA_BASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        user=cnf_dict['DATABASE']['db_user'],
        password=cnf_dict['DATABASE']['password'],
        host=cnf_dict['DATABASE']['host'],
        port=cnf_dict['DATABASE']['port'],
        database=cnf_dict['DATABASE']['db_name'])
    engine = create_engine(
        DATA_BASE_URL
    )
    return engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_db_connection().engine)
session = SessionLocal()
Base = declarative_base()
