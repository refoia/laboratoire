import requests
from bs4 import BeautifulSoup

# Fonction qui récupère le prix d'un produit sur un site donné
def get_price(product_url, website):
    # Requête HTTP pour récupérer le contenu de la page
    response = requests.get(product_url)
    # Parsing du HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Recherche du prix du produit sur la page en fonction du site
    if website == "Site 1":
        price = soup.find('span', class_='price').text
    elif website == "Site 2":
        price = soup.find('span', class_='price').text
    elif website == "Site 3":
        price = soup.find('span', class_='price').text
    else:
        # Si le site n'est pas reconnu, le prix est mis à None
        price = None

    # Conversion du prix en float
    if price is not None:
        price = float(price.replace(',', '.'))

    return price

# URLs des produits à comparer sur chaque site
product_urls = {
    "Site 1": "http://www.site1.com/product1",
    "Site 2": "http://www.site2.com/product1",
    "Site 3": "http://www.site3.com/product1",
}

# Comparaison des prix des produits sur chaque site
for website, product_url in product_urls.items():
    price = get_price(product_url, website)
    print(f"{website}: {price} €")


# Ce code utilise la bibliothèque requests pour envoyer une requête HTTP et récupérer le contenu de la page web des produits, et la bibliothèque BeautifulSoup pour parser le HTML de ces pages. Ensuite, la fonction get_price() récupère le prix du produit sur la page en fonction du site, puis le convertit en float. Enfin, le code parcourt les URLs de chaque produit et affiche le prix de chaque produit sur chaque site.

# Notez que ce code n'est qu'une base de départ et pourrait être amélioré de différentes manières, par exemple en gérant les erreurs de connexion ou en ajoutant d'autres sites de comparaison.
