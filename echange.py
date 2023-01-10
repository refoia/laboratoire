import json

# Ouverture du fichier JSON
with open('D:/laboratoire/code-php-openAI/txt/data.json', 'r') as f:
    data = json.load(f)

# Génération du texte à partir des données du fichier JSON
output = "Voici les informations que j'ai trouvées dans le fichier JSON :\n"
for key, value in data.items():
    output += f"{key}: {value}\n"

# Affichage du texte généré
print(output)
# Ce code ouvre le fichier "data.json" en mode lecture 
# et utilise la fonction json.load() pour charger les 
# données du fichier dans une variable data. Il parcourt
#  ensuite les clés et valeurs du dictionnaire data et les 
# utilise pour générer du texte. Enfin, le texte généré est 
# affiché à l'aide de la fonction print().

# Vous pouvez adapter ce code en fonction de vos besoins
#  en modifiant la structure de votre fichier JSON et en
#  modifiant la façon dont les données sont utilisées pour
#  générer le texte. Par exemple, vous pouvez utiliser des boucles
#  for pour parcourir des listes de données ou des structures
#  de données plus complexes. Vous pouvez également utiliser 
# des fonctions de formatage de chaîne de caractères pour formater 
# le texte généré de manière plus précise