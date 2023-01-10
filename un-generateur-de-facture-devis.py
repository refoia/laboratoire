
# Classe Article représentant un article avec un nom, une quantité et un prix unitaire
class Article:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_price(self):
        return self.quantity * self.unit_price

# Classe Client représentant un client avec un nom, une adresse et un numéro de téléphone
class Client:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# Classe Document représentant un document avec un numéro, une date, un client et une liste d'articles
class Document:
    def __init__(self, number, date, client, articles):
        self.number = number
        self.date = date
        self.client = client
        self.articles = articles

    def get_total_price(self):
        total_price = 0
        for article in self.articles:
            total_price += article.get_total_price()
        return total_price

# Création d'un client
client = Client("John Doe", "1 Main Street, New York, NY 10001", "555-555-5555")

#-Création d'une liste d'articles
articles = [
    Article("Article 1", 10, 10.0),
    Article("Article 2", 5, 20.0),
    Article("Article 3", 1, 50.0),
]

# Création d'un document
document = Document("FACT-2020-0001", "2020-01-01", client, articles)

# Génération de la facture
print("Numéro :", document.number)
print("Date :", document.date)
print("Client :", client.name)
print("Adresse :", client.address)
print("Téléphone :", client.phone)
print("---")
print("Articles :")
for article in document.articles:
    print(f"{article.name} - Quantité : {article.quantity} - Prix unitaire : {article.unit_price:.2f} € - Prix total : {article.get_total_price():.2f} €")
print("---")
print("Prix total :", document.get_total_price())


# Ce code crée des classes Article, Client et Document qui représentent respectivement un article, un client et un document (facture ou devis). La classe Document contient une liste d'articles et une méthode get_total_price() qui retourne le prix total du document en additionnant les prix totaux de chaque article. Ensuite, le code crée un client, une liste d'articles et un document, puis génère la facture en affichant les informations sur

