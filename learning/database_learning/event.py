from sqlalchemy.event import listens_for
from models import User
import joblib

loaded_model = joblib.load("text_classification.pkl")

# Define the event listener function
@listens_for(User, 'after_insert')
def before_insert_listener(mapper, connection, target):
    predict = loaded_model.predict([target.name])
    print(f"About to insert user: {target.name} - {target.age} - {predict[0]}")
    