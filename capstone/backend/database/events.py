import joblib
import logging
from sqlalchemy.sql import text
from sqlalchemy.event import listens_for
from capstone.backend.database import (
    get_db, 
    DBConnection
    )
from capstone.backend.database.models import (
    LogsTable, 
    CategoryTable
    )


logging.getLogger(__name__)

def get_model():
    try:
        logging.info("Downloaded Model Success")
        yield joblib.load('text_classification.pkl')
    except: 
        raise FileNotFoundError("Cannot find Model location")
    
# TODO: Implement Event to Extract Summary from ChatHistory 
# Event to Extract Summary from ChatHistory
@listens_for(LogsTable, 'after_insert')
def categorize_question(mapper, connection, target):
    db: DBConnection = get_db()
    model = get_model()
    category_data = model.predict([target.question])
    db.insert(CategoryTable, question=target.question, category=category_data[0])