from sqlalchemy import Column, Integer, String, Boolean;
from pydantic import BaseModel

class Links(Base):
    __tablename__="link"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    original_url = Column(String)
    short_url = Column(String)
    user_id = Column(Integer)

class LinksCreate(BaseModel):
    title: str
    original_url: str
    short_url: str
    user_id: str

    class Config:
        populate_by_name = True