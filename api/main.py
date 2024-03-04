from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db_connect import session
from models import Links, LinksCreate
from models import Base

app = FastAPI()

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

@app.post("/links/add")
async def create_link(title:str, original_url:str, short_url:str):
     new_url= Links(title=title, original_url=original_url, short_url=short_url)
     session.add(new_url)
     session.commit()
     return {"URL Added": new_url.title}    
     
     

def create_tables():
	Base.metadata.create_all(session)
     