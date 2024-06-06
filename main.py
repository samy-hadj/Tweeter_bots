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

print("API: ")
print(api)


#Jessaye de lire dans les messages priver, si on tenvoi /fact(5) tu dois répondre 120

# # Fonction pour interpréter et traiter les commandes
# def interpret_command(command):
#     match = re.match(r'/fact\((\d+)\)', command)
#     if match:
#         number = int(match.group(1))
#         return factorial(number)
#     else:
#         return "Commande non reconnue. Utilisez /fact(n) pour calculer la factorielle."

# # Fonction pour répondre aux messages directs
# def respond_to_direct_messages():
#     dms = api.get_direct_messages(count=10)  # Récupère les 10 derniers messages directs
#     for dm in dms:
#         message_data = dm.message_create['message_data']
#         sender_id = dm.message_create['sender_id']
#         if sender_id != api.me().id:  # Ne pas répondre à soi-même
#             command = message_data['text']
#             result = interpret_command(command)
#             response = f"Le résultat est: {result}"
#             api.send_direct_message(recipient_id=sender_id, text=response)
#             api.destroy_direct_message(dm.id)  # Supprime le message direct après traitement

# # Exécution du bot à intervalles réguliers
# import time
# while True:
#     respond_to_direct_messages()
#     time.sleep(60)  # Vérifie les messages directs toutes les 60 secondes
