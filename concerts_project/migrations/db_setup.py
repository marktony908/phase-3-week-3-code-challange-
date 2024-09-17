# db_setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create SQLite engine
engine = create_engine('sqlite:///concerts.db', echo=True)

# Bind the engine to the metadata of the Base class
Base.metadata.bind = engine

# Create a configured session class
DBSession = sessionmaker(bind=engine)

# Create a session
session = DBSession()

# Create the tables in the database if they don't exist
Base.metadata.create_all(engine)
      