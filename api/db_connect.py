from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# url = URL.create(
#     drivername="postgresql",
#     username="postgres",
#     host="localhost",
#     database="url_short",
#     port=5432
# )

# engine = create_engine(url)
# Session = sessionmaker(bind=engine)
# session = Session()
