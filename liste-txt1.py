# Ouverture du fichier en mode lecture
with open("D:/laboratoire/code-php-openAI/txt/words.txt", "r") as f:
    # Lecture des lignes du fichier
    words_list = f.readlines()
    
# Affichage du contenu de la liste
print(words_list)


# Vous pouvez utiliser la fonction readlines() pour lire le contenu d'un fichier .txt 
# et le stocker dans une liste en Python. Voici un exemple de code qui lit les lignes
#  d'un fichier words.txt, les stocke dans une liste words_list, et ensuite affiche le contenu de cette liste :