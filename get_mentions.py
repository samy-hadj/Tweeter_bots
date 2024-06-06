import tweepy

# Votre Bearer Token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAHCuuAEAAAAAZYNzRx%2BE9kU7FjD74PV2E2kDDzE%3DpIc3Coz1Ccz0NfSgX1AVZSZIgnMyQzWxmPzENJHcnh3uK6rlU5'

# Authentification
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Remplacez 'your_username' par votre nom d'utilisateur Twitter
username = 'briacsix'

# Obtenir les informations de l'utilisateur
user_response = client.get_user(username=username)

# Extraire l'ID utilisateur
user_id = user_response.data.id
print(f"Votre ID utilisateur est : {user_id}")

# Récupérer les mentions
response = client.get_users_mentions(id=user_id, max_results=10)  # Ajustez le nombre de résultats selon vos besoins

# Afficher les mentions
if response.data:
    for mention in response.data:
        print(f"User ID {mention.author_id} mentioned you in: {mention.text}")
else:
    print("No mentions found")
