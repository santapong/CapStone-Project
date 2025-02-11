from sqlalchemy.event import listens_for
from capstone.backend.database.models import (
    ChatHistory, 
    Summary
    )

from sqlalchemy.orm import Session

# TODO: Implement Event to Extract Summary from ChatHistory 
# Event to Extract Summary from ChatHistory
@listens_for(ChatHistory, 'after_insert')
def update_summary(mapper, connection, target):
    pass