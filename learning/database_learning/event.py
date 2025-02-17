from sqlalchemy.event import listens_for
from models import User

# Define the event listener function
@listens_for(User, 'after_insert')
def before_insert_listener(mapper, connection, target):
    print(f"About to insert user: {target.name}  {target.age}")
    