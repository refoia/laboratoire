# On demande à l'utilisateur d'entrer une liste de nombres
list1_input = input("Entrez une liste de nombres séparés par des virgules : ")

# On sépare la chaîne de caractères entrée par l'utilisateur en une liste de nombres
list1 = [int(x) for x in list1_input.split(",")]

# On affiche la liste
print("Voici la liste des nombres entrée :", list1)


 
list2 = [ 12,66,4,71,73]

# On utilise la fonction "all" pour vérifier que tous les éléments de la liste sont identiques
if all(x == list1[0] for x in list1):
  print("La liste 1 ne contient qu'un seul type d'élément")
else:
  print("La liste 1 contient plusieurs types d'éléments")

# On utilise la fonction "all" pour vérifier que tous les éléments de la liste sont identiques
if all(x == list2[0] for x in list2):
  print("La liste 2 ne contient qu'un seul type d'élément")
else:
  print("La liste 2 contient plusieurs types d'éléments")

# On utilise la fonction "==" pour vérifier si les deux listes sont identiques
if list1 == list2:
  print("Les listes sont identiques")
else:
  print("Les listes ne sont pas identiques")
