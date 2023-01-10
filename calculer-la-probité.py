# Fonction pour calculer la probité
def calculer_probite(score, total):
  # Vérifiez si le score et le total sont des nombres valides
  if not isinstance(score, (int, float)) or not isinstance(total, (int, float)):
    return 0

  # Vérifiez si le score est supérieur au total
  if score > total:
    return 1

  # Calculez la probité
  probite = (score - 0.5) / total

  # Retournez la probité arrondie à deux décimales
  return round(probite, 2)

# Exemple d'utilisation de la fonction
score = 369
total = 50
probite = calculer_probite(score, total)
print(f"La probité est de : {probite}")

# Ce code définit une fonction calculer_probite() 
# qui prend en entrée un score et un total, et qui renvoie la probité correspondante.
#  La probité est calculée en utilisant la formule suivante :

# probite = (score - 0.5) / total

# La fonction arrondit ensuite le résultat à deux décimales.

# Vous pouvez utiliser cette fonction en lui passant votre score et votre total
#  en tant qu'arguments, comme dans l'exemple ci-dessus. La probité sera alors 
# calculée et affichée à l'écran.




