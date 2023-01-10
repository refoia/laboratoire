# Ouvrir le fichier en mode lecture
with open('D:/laboratoire/code-php-openAI/txt/mon_fichier.txt', 'r') as f:
  # Itérer sur chaque ligne du fichier
  for line in f:
    # Traiter la ligne et les données qu'elle contient
    data = line.strip().split(',')
    # Afficher les données de la ligne
    print(data)

# Ce code ouvre le fichier mon_fichier.txt en mode lecture et utilise 
# une boucle for pour itérer sur chaque ligne du fichier. Pour chaque ligne,
#  le code utilise la méthode strip() pour enlever les espaces en début
#  et fin de ligne, et la méthode split(',') pour séparer les différentes 
# données contenues dans la ligne en utilisant la virgule comme séparateur.
#  Enfin, le code affiche les données de la ligne en utilisant la fonction print().

# Ce code peut être adapté selon vos besoins, par exemple en modifiant
#  le séparateur utilisé pour séparer les données dans chaque ligne 
# ou en effectuant des opérations spécifiques sur ces données
#  une fois qu'elles ont été lues.
 