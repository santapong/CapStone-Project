import os
import logging
from dotenv import load_dotenv
from typing import List, Optional, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Query,
    Session,
    sessionmaker,
    )
from capstone.backend.database.models import DATABASE_MODEL, DocumentTable

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
SQLLITE_URL = f'sqlite:///{SQLLITE_PATH}/database/history_database/internal.db'

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

    # Get session to database
    def get_session(self)-> Session:
        return self.session

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
               )-> None:
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
    
    results = test.query(
        table=DocumentTable
    )
    for row in results:
        print(row.ids)
        print(type(row.ids))
    
    delete_target = ['06b75c94-00a8-4adc-abab-08116d94c12d', '8c0a649a-5d3a-4b2d-a7a1-c506a646c36c', '65f3d60a-2e7b-4d75-8b97-a3f7aeba8759', '5244acd3-e09a-4bd3-ab73-ace5ddd31b99', 'e396eeaf-26ef-4aff-af69-031ec1cfd666', '471c4654-b598-4b58-bb95-d723c8dff944', '0452cd9e-4fbc-4282-b0cf-9953929d049d', '50dce891-a19d-4197-a49e-15ea125dd354', 'faea1076-cf15-4501-8790-853f47729d06', 'f9c3cadf-422e-47e8-a104-b4146e45bebf', '771c32c3-3440-4705-8537-372ba421b818', '85f7cc1f-8c14-4da8-9802-df2220138ef3', 'bba290d0-907f-4288-b7c3-db50fd5e1cd1']
    test.delete(table=DocumentTable,
                ids=delete_target)