from sqlalchemy import Column, Integer, String, UniqueConstraint
from pydantic import BaseModel, Field 


from config import settings
from models.base import Base

import bcrypt

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(225), unique=True)
    hashed_password = Column(String)

    UniqueConstraint("email", name="uq_user_email")


    def __repr__(self):
        return f"<User {self.email!r}>"
    
    @staticmethod
    def hash_password(password) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def validata_password(self, pwd):
        return bcrypt.checkpw(password=pwd.encode(), hashed_password=self.hashed_password.encode())
    
# Above is to securely have passwords

class UserBaseSchema(BaseModel):
    email: str

# this will ingherit the above email bc of it's schema
class UserSchema(UserBaseSchema):
    id: int

    class Config:
        populate_by_name = True

# Below is for creating account and logging in?? We don't want this to be thrown around often for security 
class UserAccountSchema(UserBaseSchema):
    hashed_password: str = Field(alias="password")