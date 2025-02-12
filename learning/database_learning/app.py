from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
import learning.database_learning.event  # Importing the listeners so they get registered

# Set up the engine, create the tables, and start a session
engine = create_engine('sqlite:///./mydatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name="John Doe", age=30)
session.add(new_user)
session.commit()  # This will trigger the `before_insert` event and print the message
