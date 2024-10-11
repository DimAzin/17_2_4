# create_db.py
from backend.db_depends import engine
from models.user import Base

Base.metadata.create_all(bind=engine)
