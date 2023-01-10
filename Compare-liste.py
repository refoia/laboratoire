numbers = [1, 2, 3, 4, 5]

# On initialise les variables min et max avec le premier élément de la liste
min = numbers[0]
max = numbers[0]

# On parcourt tous les éléments de la liste
for number in numbers:
  # Si l'élément est plus petit que le minimum actuel, on met à jour le minimum
  if number < min:
    min = number
  # Si l'élément est plus grand que le maximum actuel, on met à jour le maximum
  if number > max:
    max = number

# On affiche le résultat
print("Le plus petit nombre de la liste est", min)
print("Le plus grand nombre de la liste est", max)
