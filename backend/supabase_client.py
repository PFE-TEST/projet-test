import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv("bdd.env")  # ton fichier contenant SUPABASE_URL et SUPABASE_KEY

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Crée le client Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fonctions helper pour signup/login
def signup_user(email, password):
    res = supabase.auth.sign_up({"email": email, "password": password})
    return res

def login_user(email, password):
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return res