words = ["chat", "chien", "oiseau", "souris", "léopard"]

# Ouverture du fichier en mode écriture
with open("D:/laboratoire/code-php-openAI/txt/words.txt", "w") as f:
    # boucle pour écrire chaque mot sur une ligne séparée
    for word in words:
        f.write(word + "\n")
        
# Ouverture du fichier en mode lecture
with open("D:/laboratoire/code-php-openAI/txt/words.txt", "r") as f:
    # Lecture du contenu du fichier
    print(f.read())
