



import json

# Chargement du contenu du fichier JSON
with open("D:/laboratoire/code-php-openAI/trades.json", "r") as f:
  data = json.load(f)

# Recherche de la donnée précise dans le fichier JSON
for item in data:
  if item["quantity"] == "10":
    # La donnée a été trouvée
    print(item)

# Ce code lit le contenu du fichier JSON en utilisant la fonction json.load() et le stocke dans une variable data. Il parcourt ensuite chaque élément de la variable data et vérifie si la valeur de la clé "key" est égale à "value". Si c'est le cas, l'élément est affiché à l'aide de la fonction print().

# Notez que ce code est un exemple simple pour illustrer comment effectuer une recherche dans un fichier JSON en Python. Vous pouvez facilement adapter cette approche à vos propres besoins en modifiant les conditions de recherche et les actions à effectuer lorsque la donnée est trouvée.






