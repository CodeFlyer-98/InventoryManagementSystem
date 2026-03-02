from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
DATABASE_URL=os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL="postgresql://postgres:1234@localhost:5432/telusko"
engine=create_engine(DATABASE_URL)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

