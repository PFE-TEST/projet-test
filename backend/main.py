# main.py

from fastapi import FastAPI, Body
from base import things_collection   # MongoDB
from supabase_client import signup_user, login_user  # Supabase Auth
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # pour dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "Backend connecté à MongoDB et Supabase !"}


@app.get("/things")
def get_things():
    # Lire tous les objets de la collection
    return list(things_collection.find({}, {"_id": 0}))



@app.post("/signup")
def signup(data: dict = Body(...)):
    email = data.get("email")
    password = data.get("password")
    return signup_user(email, password)

@app.post("/login")
def login(data: dict = Body(...)):
    email = data.get("email")
    password = data.get("password")
    return login_user(email, password)