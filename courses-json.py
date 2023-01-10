
# Vous pouvez également charger le contenu du fichier "courses.json" en utilisant la fonction json.loads() de la bibliothèque json, comme ceci :

import json

# Chargement du contenu du fichier "courses.json"
with open("courses.json", "r") as f:
  courses_json = f.read()

# Conversion de la chaîne de caractères JSON en liste
courses = json.loads(courses_json)

# Affichage de la liste de courses
print(courses)

tech1 = courses
# print(tech1)


if tech1 == ["pain", "beurre", "oeufs", "lait", "fruits"] :
    marge = " ok on peut manger";
    print(marge)	
else :
        print(" nan ne vaut pas 1 ")	
        


# Ce code lit le contenu du fichier "courses.json",
#  le convertit en chaîne de caractères JSON et
#  utilise la fonction json.loads() pour le convertir en
# liste Python. La liste est ensuite
#  affichée à l'aide de la fonction print().

