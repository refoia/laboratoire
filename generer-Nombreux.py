import random

# Demande à l'utilisateur de saisir le chiffre à chercher
target = int(input("Entrez le chiffre à chercher: "))

# Initialise le compteur à 0
count = 0

# Réalise 50 tirages aléatoires
for i in range(50):
  # Génère un nombre aléatoire entre 0 et 9
  number = random.randint(0, 9)
  # Vérifie si le nombre est égal au chiffre cible
  if number != target:
    # Si ce n'est pas le cas, incrémente le compteur
    count += 1

# Affiche le résultat
print("Le chiffre", target, "n'est pas sorti", count, "fois sur 50 tirages.")


# Dans cet exemple, le programme demande à l'utilisateur de saisir le chiffre 
# à chercher et utilise la fonction "randint" de la bibliothèque "random" pour
#  générer 50 nombres aléatoires entre 0 et 9. Pour chaque nombre généré, 
# il vérifie si ce n'est pas le chiffre cible et incrémente le compteur
#  si c'est le cas. Enfin, il affiche le résultat.

