# Importe la bibliothèque math pour avoir accès aux fonctions mathématiques
import math

# Résout l'équation x^2 + 3x + 2 = 0
a = 1
b = 3
c = 2

# Calcule le discriminant
discriminant = b**2 - 4*a*c

# Calcul des racines de l'équation
if discriminant > 0:
    # Racines réelles et distinctes
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Les racines de l'équation sont {root1} et {root2}.")
elif discriminant == 0:
    # Racine double
    root = -b / (2*a)
    print(f"L'équation a une racine double : {root}.")
else:
    # Racines complexes
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Les racines de l'équation sont {real} + {imag}i et {real} - {imag}i.")
