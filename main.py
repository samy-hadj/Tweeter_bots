import os
import tweepy
import re
from math import factorial
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Afficher les variables d'environnement pour vérification
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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

# Optionnel: Afficher la documentation de l'API
print("Les informations sur l'API ont été enregistrées dans le fichier api_info.txt.")

# Code un truc ici qui utilise l'API
# # Récupération des tendances actuelles sur Twitter
# trends = api.get_place_trends(id=1)  # Récupère les tendances pour un endroit donné (ici, le monde entier)

# # Affichage des tendances
# print("Tendances actuelles sur Twitter :")
# for trend in trends[0]['trends']:
#     print(trend['name'])


# Récupération des derniers tweets d'un utilisateur spécifique
# user_tweets = api.user_timeline(screen_name='twitter', count=5)  # Récupère les 5 derniers tweets de Twitter

# # Affichage des tweets
# print("Derniers tweets de Twitter :")
# for tweet in user_tweets:
#     print(tweet.text)