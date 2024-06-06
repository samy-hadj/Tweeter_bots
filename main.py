import os
import tweepy
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les clés et les jetons d'accès de votre fichier .env

# Authentification OAuth 2.0
# consumer_key = os.getenv('CONSUMER_KEY_V2')
# consumer_secret = os.getenv('CONSUMER_SECRET_V2')
# bearer_token = os.getenv('BEARER_TOKEN')
# # Configuration de l'authentification OAuth 2.0
# auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

# Authentification OAuth 1.0
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
# Configuration de l'authentification OAuth 1.0
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Création de l'objet API
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

# Récupération des Tweets de l'utilisateur spécifié
utilisateur_cible = "SamyHadj2"  # Remplacez par le nom d'utilisateur souhaité
tweets = api.user_timeline(screen_name=utilisateur_cible)

# Affichage des Tweets
print(f"Tweets de @{utilisateur_cible}:")
for tweet in tweets:
    print(tweet.text)