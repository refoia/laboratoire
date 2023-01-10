# Ouverture du fichier en mode lecture
with open("D:/laboratoire/code-php-openAI/txt/words.txt", "r") as f:
    # Lecture des lignes du fichier
    words_list = f.readlines()
    words_list = [line.rstrip("\n") for line in words_list]
    
# Affichage du contenu de la liste
print(words_list)

#
ls = ['liste', 'element', 'python']
matches = [match for match in ls if "python" in match]
print(matches)


veriff = [match for match in words_list if "chat" in match]
print(veriff)
# La fonction readlines() lit toutes les lignes d'un fichier et les renvoie sous forme d'une liste, où chaque élément de la liste est une ligne du fichier. En utilisant cette fonction pour lire le contenu du fichier words.txt, nous pouvons ensuite stocker ces lignes dans la liste words_list.

# Il est à noter que la fonction readlines() gardera les sauts de ligne "\n" à la fin de chaque ligne si il y en a, si vous souhaitez enlever ces caractères vous pourriez utiliser rstrip("\n") qui supprime ce caractère de chaque élément de la liste.