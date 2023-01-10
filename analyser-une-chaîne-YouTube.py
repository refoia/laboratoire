import pandas as pd

# Chargement des données de la chaîne YouTube à partir d'un fichier CSV
df = pd.read_csv("youtube_data.csv")

# Calcul du nombre total de vues
total_views = df["views"].sum()
print(f"Nombre total de vues : {total_views:,}")

# Calcul du nombre moyen de vues par vidéo
mean_views = df["views"].mean()
print(f"Nombre moyen de vues par vidéo : {mean_views:,}")

# Calcul du pourcentage de vidéos qui ont plus de 1 000 vues
high_views = df[df["views"] > 1000]
high_view_pct = (len(high_views) / len(df)) * 100
print(f"Pourcentage de vidéos avec plus de 1 000 vues : {high_view_pct:.2f}%")

# Tri des vidéos par nombre de vues et affichage des 10 vidéos les plus populaires
most_popular = df.sort_values("views", ascending=False).head(10)
print(most_popular[["title", "views"]])

# Ce code charge d'abord les données de la chaîne YouTube à partir d'un fichier CSV en utilisant la fonction read_csv de Pandas. Il calcule ensuite le nombre total de vues, le nombre moyen de vues par vidéo et le pourcentage de vidéos qui ont plus de 1 000 vues en utilisant différentes fonctions de Pandas, telles que sum, mean et len. Enfin, il trie les vidéos par nombre de vues et affiche les 10 vidéos les plus populaires en utilisant la fonction sort_values et la méthode head.

# Il est important de noter que ce code est un exemple générique et qu'il peut être nécessaire de l'adapter en fonction de la structure de vos données et de vos objectifs spécifiques. Si vous avez des questions sur l'utilisation de Pandas ou sur la manière de charger des données à partir d'un fichier CSV, n'hésitez pas à me poser d'autres questions.

