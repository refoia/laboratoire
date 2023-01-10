# Création de la to-do list
todo_list = []

# Ajout des tâches à la liste
# Court terme
todo_list.append(("Terminer la rédaction du rapport", "Rédiger", "Court terme", 1, 60))
todo_list.append(("Envoyer le courriel de relance", "Envoyer", "Court terme", 2, 15))

# Moyen terme
todo_list.append(("Préparer le prochain atelier de formation", "Préparer", "Moyen terme", 3, 120))
todo_list.append(("Réviser le prochain examen", "Réviser", "Moyen terme", 4, 180))

# Long terme
todo_list.append(("Développer le prochain projet de recherche", "Développer", "Long terme", 5, 300))
todo_list.append(("Écrire un nouveau livre", "Écrire", "Long terme", 6, 450))

# Marge pour les imprévus
todo_list.append(("Gérer les imprévus", "Gérer", "Imprevus", 7, -1))

# Affichage de la to-do list
for task in todo_list:
    description, verbe, duree, priorite, temps = task
    print(f"{verbe} {description} ({duree} - Priorité {priorite}) : {temps} minutes")
