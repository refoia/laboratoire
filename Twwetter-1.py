


import tweepy
import time

# Remplacer les valeurs suivantes par les clés d'accès de votre compte Twitter
consumer_key = "VOTRE_CLE_CONSUMER"
consumer_secret = "VOTRE_SECRET_CONSUMER"
access_key = "VOTRE_CLE_ACCES"
access_secret = "VOTRE_SECRET_ACCES"

# Connexion à l'API Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Mot-clé à suivre
keyword = "python"

# Fonction de réponse aux tweets
def reply_to_tweet(tweet):
    # Récupération du nom de l'utilisateur et de son écran
    username = tweet.user.screen_name
    # Construction du message de réponse
    message = f"Merci pour votre tweet sur {keyword}, @{username} ! Nous espérons que vous apprécierez Python autant que nous."
    # Envoi du tweet de réponse
    api.update_status(status=message, in_reply_to_status_id=tweet.id)

# Fonction de surveillance des tweets
def watch_tweets():
    # Récupération des tweets contenant le mot-clé
    tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(5)
    # Réponse aux tweets
    for tweet in tweets:
        reply_to_tweet(tweet)

# Boucle infinie de surveillance des tweets
while True:
    watch_tweets()
    time.sleep(60)

# Ce code utilise la fonction search_tweets de l'API Twitter pour récupérer les tweets contenant le mot-clé donné, puis envoie une réponse à chaque tweet en utilisant la fonction update_status. La fonction watch_tweets est appelée en boucle infinie toutes les 60 secondes, ce qui permet de surveiller en permanence les tweets contenant le mot-clé.


