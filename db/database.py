# database.py
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase")
database = Database(DATABASE_URL)
