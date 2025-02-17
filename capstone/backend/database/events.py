import joblib
import logging
from sqlalchemy.sql import text
from sqlalchemy.event import listens_for
from capstone.backend.database.models import (
    ChatHistoryTable, 
    CategoryTable
    )

from capstone.backend.database import get_db, DBConnection

from sqlalchemy.orm import Session

logging.getLogger(__name__)

loaded_model = joblib.load('text_classification.pkl')
logging.info("Downloaded Model Success")

# TODO: Implement Event to Extract Summary from ChatHistory 
# Event to Extract Summary from ChatHistory
@listens_for(ChatHistoryTable, 'after_insert')
def categorize_question(mapper, connection, target):
    db: DBConnection = get_db()
    category_data = loaded_model.predict([target.question])
    db.insert(CategoryTable, question=target.question, category=category_data[0])