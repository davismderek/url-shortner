from sqlalchemy import Column, Integer, String, Boolean;
from sqlalchemy.orm import declarative_base
from db_connect import engine
from pydantic import BaseModel
# from sqlalchemy.orm import relationship
# from db.base_class import Base


Base = declarative_base()

class Links(Base):
    __tablename__="link"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    original_url = Column(String)
    short_url = Column(String)
    private = Column(Boolean, default=False)
    # user_id = Column(Integer, ForeignKey("user.id"))


class LinksCreate(BaseModel):
    title: str
    original_url = str
    short_url = str


# class User(Base):
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)


Base.metadata.create_all(engine)

# nullable=False