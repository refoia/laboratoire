

import random

def generate_formula():
  # Choisir aléatoirement le nombre de termes dans la formule
  num_terms = random.randint(2, 5)
  
  # Générer aléatoirement chaque terme de la formule
  terms = [str(random.randint(1, 10)) for _ in range(num_terms)]
  
  # Choisir aléatoirement le signe à utiliser entre chaque terme
  signs = [random.choice(['+', '-', '*', '/']) for _ in range(num_terms - 1)]
  
  # Assembler la formule en utilisant les termes et les signes choisis aléatoirement
  formula = ' '.join([term + sign for term, sign in zip(terms, signs)])
  
  return formula

# Générer et afficher 10 formules mathématiques aléatoires
for i in range(25):
  formula = generate_formula()
  print(f'Formule {i+1}: {formula}')



# Ce code génère aléatoirement des formules
#  mathématiques en utilisant des entiers 
# aléatoires comme termes et en choisissant
#  aléatoirement un signe arithmétique 
# entre chaque terme. Les formules 
# générées peuvent être
#  de la forme "2 + 3 - 5", "10 * 2 / 5"
#  ou toute autre combinaison de termes 
# et de signes.

