import os
import logging

from dotenv import load_dotenv
from typing import List

load_dotenv()

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from capstone.backend.api.schema.model_database import DATABASE_MODEL

"""
################### Take Note ####################
 #   We use SQLalchemy in this project.         #
 #                                              #
 #   Database support                           #
 #   1.Postgresql database                      #
 #   2.SQLLite                                  #
 #   Comming soon...                            #
 #                                              #
##################################################

This is for Frontend Dashboard to monitor how much user asking.

 """

logging.getLogger(__name__)

# Default Database
SQLLITE_PATH = os.getenv("PYTHONPATH")
SQLLITE_URL = f'sqlite:///{SQLLITE_PATH}/capstone/backend/database/history_database/sqlalchemy_example.db'

# Database login info
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME' ,default = None)
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', default = None)
DATABASE_PORT = os.getenv('DATABASE_PORT' ,default=None)
DATABASE_DB = os.getenv('DATABASE_DB', default= None)
DATABASE_URL = os.getenv('DATABASE_URL' ,default = SQLLITE_URL)

# Database config
DATABASE_CREATE = os.getenv('DATABASE_CREATE', default=False)

# TODO: Make CRUD for this History database.
class DBConnection:

    # Initial connect to database.
    def __init__(
            self,
            create_database: bool = False,
            base_model: declarative_base = None
            ) -> None :
        
        self.engine = create_engine(DATABASE_URL)
        self.base_model = base_model
        self.session = sessionmaker(bind=self.engine)()
        if create_database:
            self.__create_database()

    # TODO: If database exist not create it.
    def __create_database(self, 
                        ) -> None :
        self.base_model.metadata.create_all(bind = self.engine)


    # Create session of history database.
    def get_session(self) -> sessionmaker:
        return self.session
    
    # Get Table inside database.
    def get_table(self):
        pass

    # Get data Table of this database.
    def query(self,
            Table
        ) -> List:
        return self.session.query(Table).all()
    
    # Get data of Table of this database by condition.
    def query_condition(self,
                        Table,
                        **kwargs
        ) -> List:
        return self.session.query(Table).filter_by(kwargs=kwargs).all()
    
    # CRUD Consept
    def update(self):
        pass


if __name__ == '__main__':
    test = DBConnection(create_database=True, base_model=DATABASE_MODEL)