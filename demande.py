
# La structure de contrôle de flux "if" permet de tester une condition et d'exécuter un bloc de code si la condition est vraie. Vous pouvez également utiliser "elif" (abréviation de "else if") pour tester d'autres conditions et "else" pour exécuter un bloc de code si aucune des conditions n'est vraie.

# Il est important de noter que les conditions doivent toujours être
#  entourées de parenthèses et que les blocs de code doivent être
#  indentés correctement pour que le programme fonctionne correctement.

# Demande à l'utilisateur de saisir les valeurs de a et b
a = float(input("Entrez la valeur de a: "))
b = float(input("Entrez la valeur de b: "))

# Vérifie si l'équation a une solution
if a == 0:
  if b == 0:
    print("L'équation a une infinité de solutions.")
  else:
    print("L'équation n'a pas de solution.")
else:
  # Calcule et affiche la solution de l'équation
  x = -b / a
  print("La solution de l'équation est x =", x)

# Dans cet exemple, le programme demande à l'utilisateur de saisir les valeurs de "a" et "b" et les stocke dans des variables. Ensuite, il vérifie si l'équation a une solution en utilisant la structure de contrôle de flux "if". Si "a" est égal à 0, l'équation peut avoir une infinité de solutions (si "b" est égal à 0) ou pas de solution (si "b" est différent de 0). Si "a" est différent de 0, le programme calcule et affiche la solution de l'équation en utilisant la formule x = -b / a.

# Il est important de noter que cet exemple ne gère que les équations du premier degré. Pour résoudre des équations de degré supérieur, vous devrez utiliser des algorithmes plus complexes, tels que 
# la méthode de Newton ou la méthode de la bissection.



# Constantes
G = 6.674e-11  # Constante de gravitation universelle en N m^2/kg^2

# Demande à l'utilisateur de saisir les masses et les distances des objets
mass1 = float(input("Entrez la masse de l'objet 1 en kg: "))
mass2 = float(input("Entrez la masse de l'objet 2 en kg: "))
distance = float(input("Entrez la distance entre les objets en m: "))

# Calcule la force de gravitation entre les objets
force = G * mass1 * mass2 / distance**2

# Affiche le résultat
print("La force de gravitation entre les objets est de", force, "N")

# Dans cet exemple, le programme demande à l'utilisateur de saisir les masses et la distance entre les objets et stocke ces valeurs dans des variables. Ensuite, il utilise la loi de gravitation universelle de Newton pour calculer la force de gravitation entre les objets et affiche le résultat.

# Il est important de noter que cet exemple ne tient pas compte de la réduction de la force de gravitation due à la distance et ne peut être utilisé que pour des objets proches de la surface de la Terre. Pour des objets à des distances plus grandes, vous devrez utiliser des modèles plus complexes de la force de gravitation, tels que la loi de gravitation de Newton modifiée de Poisson.



# Constantes
GRAVITY = 9.81  # Accélération de la gravité en m/s^2

# Demande à l'utilisateur de saisir les caractéristiques de l'objet et du fluide
density = float(input("Entrez la densité du fluide en kg/m^3: "))
volume = float(input("Entrez le volume de l'objet en m^3: "))
mass = float(input("Entrez la masse de l'objet en kg: "))

# Calcule la poussée d'Archimède
upthrust = density * volume * GRAVITY

# Calcule la force de flottaison en fonction de la poussée d'Archimède et de la masse de l'objet
floating_force = mass * GRAVITY - upthrust

# Affiche le résultat
print("La force de flottaison est de", floating_force, "N")


# Dans cet exemple, le programme demande à l'utilisateur de saisir la densité du fluide, le volume de l'objet et sa masse et stocke ces valeurs dans des variables. Ensuite, il utilise la formule de la poussée d'Archimède (F = ρVg) pour calculer la poussée d'Archimède et la force de flottaison en utilisant la masse de l'objet et l'accélération de la gravité. Enfin, il affiche le résultat.

# Il est important de noter que cet exemple ne tient pas compte de la forme de l'objet et de ses autres caractéristiques (par exemple, sa surface, sa vitesse, etc.), qui peuvent influencer la force de flottaison. Pour un calcul plus précis, vous devrez tenir compte de ces facteurs et utiliser des modèles plus complexes de la flottaison.





# Importe les modules nécessaires
import pytide
import datetime

# Demande à l'utilisateur de saisir la latitude, la longitude et la date
latitude = float(input("Entrez la latitude en degrés décimaux: "))
longitude = float(input("Entrez la longitude en degrés décimaux: "))
date = input("Entrez la date (jj/mm/aaaa): ")

# Crée un objet "HarmonicModel" avec les coefficients de marée les plus couramment utilisés
model = pytide.HarmonicModel(['M2', 'S2', 'N2', 'K1', 'O1', 'P1', 'Q1'])

# Crée un objet "Tide" avec le modèle et la position géographique
tide = pytide.Tide(model, latitude, longitude)

# Calcule la hauteur de la marée à la date spécifiée
tide_height = tide.at(datetime.datetime.strptime(date, '%d/%m/%Y'))

# Affiche la hauteur de la marée
print("Hauteur de la marée:", tide_height, "mètres")


# Dans cet exemple, le programme demande à l'utilisateur de saisir 
# la latitude, la longitude et la date et stocke ces valeurs dans des variables.
#  Ensuite, il utilise la bibliothèque "pytide" pour créer un objet "HarmonicModel" 
# avec les coefficients de marée les plus couramment utilisés et un objet "Tide" avec
#  le modèle et la position



