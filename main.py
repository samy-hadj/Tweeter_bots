import os
import tweepy
import re
from math import factorial
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Afficher les variables d'environnement pour vérification
bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
client = tweepy.Client(bearer_token, api_key, api_secret_key, access_token, access_token_secret)

# Configuration de l'authentification 
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)
# Test pour s'assurer que l'authentification a réussi
try:
    api.verify_credentials()
    print("Authentification réussie")
except Exception as e:
    print(f"Erreur lors de l'authentification : {e}")

# Enregistrer les informations dans un fichier
with open("api_info.txt", "w") as f:
    print("API Methods and Attributes: ", file=f)
    print(dir(api), file=f)

# # Optionnel: Afficher la documentation de l'API
print("Les informations sur l'API ont été enregistrées dans le fichier api_info.txt.")
# Code un truc ici qui utilise l'API
client.create_tweet(text="Hello World")
