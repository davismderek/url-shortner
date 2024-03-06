from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db_connect import session, engine
from models.links import Links, LinksCreate
from models.base import Base
from config import settings
from services import create_user, get_user
from models.users import User, UserSchema, UserAccountSchema


def create_tables():
	Base.metadata.create_all(bind=engine)
     
def start_aplication():
     app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
     create_tables()
     return app
     
app = start_aplication()
# app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Root Route"}

@app.get("/links")
def get_links():
    linkss = session.query(Links)
    return linkss.all()

@app.get("/users")
def get_users():
    users = session.query(User)
    return users.all()

@app.post("/links/add")
async def create_link(link_data: LinksCreate):
     new_url= Links(**link_data.model_dump())
     session.add(new_url)
     session.commit()
     return {"URL Added": new_url.title} 

   
     
@app.post("/register", response_model=UserSchema)
def register_user(payload: UserAccountSchema):
     payload.hashed_password = User.hash_password(payload.hashed_password)
     return create_user(user=payload)

@app.post("/login")
async def login(payload: UserAccountSchema):
     try:
          user: User = get_user(email=payload.email)
     
     except:
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail = "Invalid User Credentials"
            )
     
     is_validated: bool = user.validata_password(payload.hashed_password)

     if not is_validated: 
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Invalid User Credentials"
          )
     return {"detail": "Successful Login"}

# def create_tables():
# 	Base.metadata.create_all(session)
     