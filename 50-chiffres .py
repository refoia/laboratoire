import string
import random

# Génère une chaîne de caractères aléatoires de longueur 255
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=255))

# print(random_string)

# Voici un exemple de code Python
#  qui peut être utilisé pour trouver 4 chiffres
#   dans un tirage de 50 chiffres
# Liste des 50 chiffres du tirage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# Sélectionnez 4 chiffres au hasard dans la liste
selected_numbers = random.sample(numbers, 4)

# Vérifiez si les chiffres sont tous différents
while len(set(selected_numbers)) < 4:
  selected_numbers = random.sample(numbers, 4)

# Affichez les chiffres sélectionnés
print(selected_numbers)
liste = [1,2,3,5,10]

print(len(liste))
# Donne moi un code python pour trouver 4 chiffre dans un tirage de 50 chiffres 

# Voici un exemple de code Python qui peut être utilisé pour trouver 4 chiffres
#  dans un tirage de 50 chiffres :

 
# Liste des 50 chiffres du tirage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# Sélectionnez 4 chiffres au hasard dans la liste
selected_numbers = random.sample(numbers, 4)

# Affichez les chiffres sélectionnés
print(selected_numbers)

# Ce code utilise la fonction random.sample pour sélectionner 4 chiffres
#  au hasard dans la liste numbers. Vous pouvez utiliser cette fonction 
#  pour sélectionner n'importe quel nombre de chiffres dans la liste, en
#   changeant simplement le deuxième argument passé à la fonction.

# Il est important de noter que ce code ne garantit pas que les 4 chiffres 
# sélectionnés seront différents les uns des autres. Si vous souhaitez
#  s'assurer que les chiffres sélectionnés sont uniques, vous pouvez utiliser
#   une boucle while pour vérifier si les chiffres sont tous différents avant de les afficher.