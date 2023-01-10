import math

def solve_quadratic_equation(a, b, c):
  # Calcule les racines de l'équation du second degré ax^2 + bx + c = 0
  discriminant = b**2 - 4*a*c
  if discriminant < 0:
    print("L'équation n'a pas de solution réelle")
  elif discriminant == 0:
    x = -b / (2*a)
    print("L'équation a une solution unique:", x)
  else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("L'équation a deux solutions:", x1, "et", x2)

# Ce code imprimera "La solution de l'équation est x = 1.5".

# Vous pouvez également utiliser des bibliothèques tierces, comme NumPy, pour résoudre des équations plus complexes. Par exemple, voici comment utiliser NumPy pour résoudre un système
#  d'équations linéaires de la forme ax + by = c:


# Teste la fonction avec des valeurs de a, b
def solve_equation(a, b):
    if a == 0:
        if b == 0:
            print("L'équation a une infinité de solutions.")
        else:
            print("L'équation n'a pas de solution.")
    else:
        x = -b / a
        print("La solution de l'équation est x = {}".format(x))

# Testons la fonction en résolvant l'équation 2x - 3 = 0
solve_equation(2, -3)


# Ce code imprimera "La solution du système est x = 1.0, y = 2.0".
import numpy as np

# Définissons les coefficients de notre système d'équations sous forme de matrices
A = np.array([[2, 1], [3, 2]])
b = np.array([5, 8])

# Résolvons le système d'équations en utilisant la fonction linalg.solve() de NumPy
x = np.linalg.solve(A, b)

print("La solution du système est x = {}, y = {}".format(x[0], x[1]))

