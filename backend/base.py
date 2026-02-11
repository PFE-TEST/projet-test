# base.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Charger le fichier bdd.env
load_dotenv("bdd.env")

# Récupérer l'URI MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Créer le client MongoDB
client = MongoClient(MONGO_URI)

# Sélectionner la base de données
db = client.smart_building

# Sélectionner la collection "things"
things_collection = db.things