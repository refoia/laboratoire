

import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données depuis un fichier CSV
df = pd.read_csv('donnees_youtube.csv')

# Calcul du nombre total de vues pour chaque vidéo
df['nombre_vues'] = df['vues_debut'] - df['vues_fin']

# Calcul du taux de likes par vue
df['taux_likes'] = df['nombre_likes'] / df['nombre_vues']

# Calcul du taux d'abonnés par vue
df['taux_abonnés'] = df['nombre_abonnés'] / df['nombre_vues']

# Création d'un graphique à barres affichant le nombre de vues par vidéo
df.plot(kind='bar', x='titre', y='nombre_vues')
plt.show()

# Exportation des données au format JSON
df.to_json('donnees_youtube.json')
# Ce code utilise la bibliothèque 
# Pandas pour charger les données 
# depuis un fichier CSV, puis calcule
#  le nombre total de vues, le taux de
#  likes et le taux d'abonnés par vue
#  pour chaque vidéo. Il utilise également
#  la bibliothèque Matplotlib pour créer 
# un graphique à barres affichant le nombre
#  de vues par vidéo, et enfin exporte les données au format JSON.

#Pour tirer des insights intéressants de vos 
# données, vous pouvez utiliser des techniques 
# d'analyse statistique pour découvrir des tendances
#  et des modèles dans vos données. Par exemple,
#  vous pourriez étudier la relation entre 
# le nombre de vues et le nombre de likes
#  ou le nombre d'abonnés pour chaque vidéo, 
# ou encore comparer les taux de likes
#  et de d'abonnés par vue entre 
# différentes vidéos. Vous pouvez 
# également utiliser des outils 
# de visualisation de données 
# pour représenter graphiquement 
# vos résultats et les rendre
#  plus faciles à comprendre.