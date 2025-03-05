import joblib
import logging
from sqlalchemy.event import listens_for
from capstone.backend.database.models import (
    LogsTable, 
    CategoryTable
    )

logging.getLogger(__name__)

def get_model():
    try:
        logging.info("Downloaded Model Success")
        return joblib.load('text_classification.pkl')
    except: 
        raise FileNotFoundError("Cannot find Model location")
    
# Event to Extract Summary from Logs
@listens_for(LogsTable, 'after_insert')
def categorize_question(mapper, connection, target):
    model = get_model()
    category_data = model.predict([target.question])
    print(category_data[0])
    # Use the existing transaction via connection.execute()
    connection.execute(
        CategoryTable.__table__.insert(),
        {"question": target.question, "category": category_data[0]}
    )