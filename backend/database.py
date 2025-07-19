from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your MySQL connection string
# Example: "mysql+mysqlconnector://user:password@host/dbname"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/product_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 