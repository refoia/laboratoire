from collections import Counter

# Les données sont sous la forme d'une liste de tuples (personne, aliment préféré)
data = [("Alice", "Pizza"), ("Bob", "Poulet"), ("Charlie", "Pizza"), ("Dave", "Salade"), 
        ("Eve", "Poulet"), ("Frank", "Poulet"), ("Gary", "Poulet"), ("Holly", "Salade"), ("Lea", "Poulet")]

# Créer un compteur à partir des données
counter = Counter(data)

# Calculer la probabilité de chaque élément
total_count = sum(counter.values())
probabilities = {k: v / total_count for k, v in counter.items()}

# Afficher l'arbre de probabilité
for person, food in probabilities.items():
  print(f"La probabilité que {person[0]} aime {person[1]} est de {food:.2f}")
