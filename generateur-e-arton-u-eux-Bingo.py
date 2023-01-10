
import random

# Nombre de colonnes et de lignes du carton
COLUMNS = 5
ROWS = 5

# Nombres disponibles dans le carton (de 1 à 75)
numbers = list(range(1, 76))

# Génération du carton
card = []
for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        # Choix d'un nombre au hasard parmi les nombres restants
        index = random.randint(0, len(numbers)-1)
        number = numbers[index]
        # Ajout du nombre au carton et suppression de la liste des nombres restants
        row.append(number)
        del numbers[index]
    # Ajout de la ligne au carton
    card.append(row)

# Affichage du carton
for row in card:
    print(row)


# Ce code utilise la bibliothèque random pour générer des nombres aléatoires. Il crée une liste de nombres disponibles (numbers) et une liste vide pour stocker le carton (card). Ensuite, il parcourt chaque ligne et chaque colonne du carton et choisit un nombre au hasard parmi les nombres restants. Le nombre est ajouté au carton et supprimé de la liste des nombres restants afin qu'il ne soit pas sélectionné à nouveau. Enfin, le code affiche le carton en parcourant chaque ligne de la liste.

# Notez que ce code génère aléatoirement un carton de Bingo unique à chaque exécution, mais il est possible de l'adapter pour générer plusieurs cartons à la fois ou pour respecter certaines contraintes (par exemple, chaque ligne doit contenir un nombre parmi les 5 premiers, les 5 suivants, etc.).
