
# Demande à l'utilisateur de saisir les dépenses
depenses = []
depense = input("Entrez une dépense (ou tapez 'stop' pour arrêter) : ")

while depense != "stop":
  depenses.append(float(depense))
  depense = input("Entrez une dépense (ou tapez 'stop' pour arrêter) : ")

# Calcule la somme des dépenses
total_depenses = sum(depenses)

# Affiche le total des dépenses
print("Le total des dépenses est de", total_depenses, "euros.")


# Ce code demande à l'utilisateur de saisir chaque dépense individuellement,
#  en utilisant une boucle "while" qui s'arrête lorsque l'utilisateur tape "stop".
#  Les dépenses sont stockées dans une liste, et la somme des dépenses est calculée
#  en utilisant la fonction "sum()". Enfin, le total des dépenses est affiché à l'écran.

# Il est possible de personnaliser ce code en fonction de vos besoins, par exemple
#  en ajoutant des fonctionnalités pour gérer différentes catégories de dépenses ou 
# pour enregistrer les dépenses dans un fichier.