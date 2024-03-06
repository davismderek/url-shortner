from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel
from models.base import Base
from .users import User

class Links(Base):
    __tablename__="link"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    original_url = Column(String)
    short_url = Column(String)
    user_id = mapped_column(ForeignKey(User.id))

class LinksCreate(BaseModel):
    title: str
    original_url: str
    short_url: str
    user_id: int

    class Config:
        populate_by_name = True