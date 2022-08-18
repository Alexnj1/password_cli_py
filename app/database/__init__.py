from sqlalchemy import create_engine
# Import declarative_base class that table classes will inherit from
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import dotenv

# Base class for table classes
Base = declarative_base()

# Session class to inherit from to be able to carry out database transactions, CRUD
Session = sessionmaker()

# Create an engine to specify the database to be used as well as options for the database
dotenv.load_dotenv()
engine = create_engine(os.getenv("DB_URL"), echo = True)

# Create's database with metadata based on the Base class, Table class and the engine
Base.metadata.create_all(engine)

# print(sqlalchemy.__version__) 1.4.40