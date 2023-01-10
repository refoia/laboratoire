


import requests
from bs4 import BeautifulSoup

# Définissons l'URL de la page que nous voulons scraper
url = "https://www.example.com"

# Envoyons une requête HTTP GET à l'URL et récupérons le contenu de la page
response = requests.get(url)
content = response.content

# Créons un objet BeautifulSoup à partir du contenu de la page
soup = BeautifulSoup(content, "html.parser")

# Récupérons tous les éléments HTML de la page qui ont la classe "article-title"
titles = soup.find_all(class_="article-title")

# Pour chaque élément trouvé, imprimons son contenu texte
for title in titles:
    print(title.text)




# Ce code envoie une requête HTTP GET à l'URL spécifiée, récupère le contenu de la page, puis utilise BeautifulSoup pour parser le contenu HTML et extraire tous les éléments qui ont la classe "article-title". Enfin, il imprime le contenu texte de chaque élément trouvé.

# Vous pouvez personnaliser ce code en fonction de vos besoins en modifiant l'URL, en utilisant différents filtres de sélection et en traitant les données extraites de manière différente.



