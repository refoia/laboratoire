# Voici un exemple de code en Python pour créer un moteur de recherche internet simple:

# Copy code
import requests

def search(query):
  url = "https://www.google.com/search?q=" + query
  r = requests.get(url)
  return r.text

query = input("Entrez votre recherche: ")
result = search(query)
print(result)
# Ce code utilise la bibliothèque requests pour envoyer une requête HTTP GET à Google avec la recherche spécifiée par l'utilisateur. Le résultat de la recherche est renvoyé sous forme de texte HTML, qui peut être affiché ou traité ultérieurement.

# Notez que ce code ne fonctionnera que si vous avez installé la bibliothèque requests en utilisant la commande pip install requests.

# Ce code de base peut être étendu de différentes manières pour ajouter des fonctionnalités supplémentaires, telles que la pagination des résultats, la recherche dans d'autres moteurs de recherche ou l'affichage des résultats de manière plus conviviale.