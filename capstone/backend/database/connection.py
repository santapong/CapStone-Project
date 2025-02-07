import os
import logging
from dotenv import load_dotenv
from typing import List, Optional, Any
from typing_extensions import Self
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Query,
    sessionmaker, 
    declarative_base,
    )
from capstone.backend.database.model_database import DATABASE_MODEL

load_dotenv()

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
SQLLITE_URL = f'sqlite:///{SQLLITE_PATH}/database/history_database/sqlalchemy_example.db'

# Database login info
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME' ,default = None)
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', default = None)
DATABASE_PORT = os.getenv('DATABASE_PORT' ,default=None)
DATABASE_DB = os.getenv('DATABASE_DB', default= None)
DATABASE_URL = os.getenv('DATABASE_URL' ,default = SQLLITE_URL)

# Database config
DATABASE_CREATE = os.getenv('DATABASE_CREATE', default=False)

class DBConnection:
    def __init__(
        self,
    ):
        """
        Initialize the database connection.

        :param database_url: The database URL for connection.
        :param base_model: The SQLAlchemy declarative base containing your table definitions.
        :param create_database: If True, creates tables if they do not exist.
        """
        self.engine = create_engine(DATABASE_URL)
        self.base_model = DATABASE_MODEL
        self.session = sessionmaker(bind=self.engine)()
        self.__create_tables()

    def __create_tables(self) -> None:
        """
        Create all tables defined in the base model if they do not already exist.
        """
        if not self.base_model:
            raise ValueError("Base model is not defined. Cannot create tables.")
        
        try:
            self.base_model.metadata.create_all(bind=self.engine, checkfirst=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create tables: {e}")
        
    # Get table inside database.
    def get_table(self):
        return self.base_model.metadata.tables

    # Query data from table of this database.
    def query(
            self,
            table,
            limit:  Optional[List[Any]] = None,
            offset: Optional[List[Any]] = None,
            filters: Optional[List[Any]] = None,
            order_by: Optional[List[Any]] = None,
        )-> List:
        try:
            # Build the query
            query: Query = self.session.query(table)

            # Apply filters if provided >> Where clause
            if filters:
                query = query.filter(*filters)

            # Apply ordering if provided >> Order by clause
            if order_by:
                query = query.order_by(*order_by)

            # Apply limit and offset in one step if applicable >> Limit and Offset clause
            if limit is not None or offset is not None:
                query = query.limit(limit).offset(offset or 0)

            # Execute and return results
            return query.all()

        except Exception as e:
            print(f"Query error on table {table.__tablename__}: {e}")
            return []
    
    # Insert Data to table of this database.
    def insert(
            self,
            table,
            **kwargs
        ) -> None:
        try:
            self.session.add(table(**kwargs))
            self.session.commit()
            print(f"Insert Success for {kwargs.items()}")
        except:
            self.session.rollback()
            raise Exception(f"Insert Error from table {table.__tablename__}")
        finally:
            self.session.close()

    # Delete Data to table of this database.
    def delete(
            self,
            table,
            **kwargs
               ):
        try:
            self.session.query(table).filter_by(**kwargs).delete()
            self.session.commit()
            print(f"Delete Success for {kwargs.items()}")
        except:
            self.session.rollback()
            raise Exception(f"Delete Error from table {table.__tablename__}")
        finally:
            self.session.close()
        
# Database session
def get_db():
    db: DBConnection = DBConnection()
    try:
        print('Database connected')
        yield db
    finally:
        db.session.close()

if __name__ == '__main__':
    test = DBConnection()