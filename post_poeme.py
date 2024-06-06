import os
import tweepy
from dotenv import load_dotenv
from openai import OpenAI

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Afficher les variables d'environnement pour vérification
bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Configurer l'authentification Twitter
client = tweepy.Client(bearer_token, api_key, api_secret_key, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

# Configurer l'authentification OpenAI
openai_client = OpenAI(api_key=openai_api_key)

# Test pour s'assurer que l'authentification a réussi
try:
    api.verify_credentials()
    print("Authentification réussie")
except Exception as e:
    print(f"Erreur lors de l'authentification : {e}")

def generate_poem():
    prompt = "Écris un poème en français sur le thème de la nature, de 250 caractères ou moins."
    completion = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    poem = completion.choices[0].message.content.strip()
    return poem

def tweet_poem(poem):
    try:
        if len(poem) <= 280:
            client.create_tweet(text=poem)
            print("Poème tweeté avec succès")
        else:
            print("Erreur : Le poème généré dépasse la limite de 280 caractères.")
    except Exception as e:
        print(f"Erreur lors de la publication du poème : {e}")

# Générer un poème et le publier sur Twitter
poem = generate_poem()
print(f"Poème généré : {poem}")
tweet_poem(poem)
