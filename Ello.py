import math

# Demande à l'utilisateur de saisir les dimensions de l'objet
longueur = float(input("Entrez la longueur de l'objet : "))
largeur = float(input("Entrez la largeur de l'objet : "))
hauteur = float(input("Entrez la hauteur de l'objet : "))
rayon = float(input("Entrez le rayon de l'objet : "))

# Calcule le volume de l'objet en fonction de sa forme
if longueur == largeur == hauteur:  # cube
  volume = longueur ** 3
elif rayon != 0:  # cylindre ou sphère
  if hauteur != 0:
    volume = math.pi * rayon ** 2 * hauteur
  else:
    volume = 4/3 * math.pi * rayon ** 3
else:  # parallélépipède rectangle
  volume = longueur * largeur * hauteur

# Affiche le volume de l'objet
print("Le volume de l'objet est de", volume, "cm³.")

# Ce code demande à l'utilisateur de saisir les dimensions de l'objet, 
# puis utilise une instruction "if" pour déterminer sa forme et sélectionner
#  la formule appropriée pour calculer son volume. Le volume est ensuite affiché à l'écran.

# Il convient