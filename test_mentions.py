import os
import tweepy
import time
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

# Configurer l'authentification Twitter avec l'API v2
client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret_key, access_token=access_token, access_token_secret=access_token_secret)

# Configurer l'authentification OpenAI
openai_client = OpenAI(api_key=openai_api_key)

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

def reply_to_mentions():
    since_id = None
    while True:
        new_since_id = since_id
        # Récupère les mentions en utilisant l'API v2
        mentions = client.get_users_mentions(id="eHJRZnlxNUZsUXR0UldheERkd1M6MTpjaQ", since_id=since_id)
        if mentions.data:
            for mention in mentions.data:
                new_since_id = max(mention.id, new_since_id)
                if mention.in_reply_to_user_id is not None:
                    continue
                print(f"Répondre à {mention.author_id}")
                poem = generate_poem()
                try:
                    client.create_tweet(
                        text=f"@{mention.author_id} {poem}",
                        in_reply_to_tweet_id=mention.id,
                    )
                    print("Poème tweeté avec succès")
                except Exception as e:
                    print(f"Erreur lors de la publication du poème : {e}")
        since_id = new_since_id
        time.sleep(60)  # Attendre 60 secondes avant de vérifier à nouveau les mentions

if __name__ == "__main__":
    reply_to_mentions()
