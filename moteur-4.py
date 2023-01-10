import numpy as np

# les données d'entraînement sont un tableau de distances parcourues (en km)
X = np.array([100, 200, 300, 400, 500])

# les étiquettes sont les quantités de carburant utilisées (en litres)
y = np.array([10, 20, 30, 40, 50])

# calcul de la régression linéaire
a, b = np.polyfit(X, y, 1)

# affichage des résultats
print("Pente de la régression linéaire :", a)
print("Ordonnée à l'origine :", b)

# prédiction de la consommation de carburant pour une distance de 300 km
prediction = a * 600 + b
# print("Prédiction de la consommation de carburant :", prediction, "litres")

# Ce code crée une régression linéaire à partir de données d'entraînement et utilise 
# cette régression pour faire une prédiction sur la consommation de carburant pour une
#  distance donnée. Bien sûr, il existe de nombreuses autres façons de créer une IA et 
# cet exemple ne constitue qu'une introduction simplifiée.
