
import json

# Création de la liste de courses
courses = ["pain", "beurre", "oeufs", "lait", "fruits","farine"]

# Conversion de la liste en chaîne de caractères JSON
courses_json = json.dumps(courses)

# Enregistrement de la chaîne de caractères JSON dans un fichier
with open("D:/laboratoire/code-php-openAI/txt/courses1.json", "w") as f:
  f.write(courses_json)

# Ce code crée une liste de courses en Python et utilise la fonction json.dumps() pour la convertir en chaîne de caractères JSON. La chaîne de caractères JSON est ensuite enregistrée dans un fichier nommé "courses.json".

# Si vous ouvrez le fichier "courses.json" dans un éditeur de texte, vous devriez voir le contenu de la liste de courses au format JSON, comme ceci :



