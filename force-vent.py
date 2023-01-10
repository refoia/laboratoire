

# Demande à l'utilisateur de saisir la vitesse du vent en nœuds
wind_speed = float(input("Entrez la vitesse du vent en nœuds: "))

# Calcule la force du vent selon la formule de Beaufort
if wind_speed < 1:
  wind_force = 0
elif wind_speed < 4:
  wind_force = 1
elif wind_speed < 7:
  wind_force = 2
elif wind_speed < 11:
  wind_force = 3
elif wind_speed < 17:
  wind_force = 4
elif wind_speed < 22:
  wind_force = 5
elif wind_speed < 28:
  wind_force = 6
elif wind_speed < 34:
  wind_force = 7
elif wind_speed < 41:
  wind_force = 8
elif wind_speed < 48:
  wind_force = 9
elif wind_speed < 56:
  wind_force = 10
elif wind_speed < 64:
  wind_force = 11
else:
  wind_force = 12

# Affiche le résultat
print("La force du vent est de", wind_force)







# Dans cet exemple, le programme demande à l'utilisateur de saisir la vitesse du vent en nœuds (unité de mesure de la vitesse du vent) et calcule la force du vent en utilisant la formule de Beaufort, qui associe une force à chaque intervalle de vitesse. La force du vent est une échelle de 0 à 12 qui indique l'intensité du vent en fonction de sa vitesse.

# Il est important de noter que cet exemple ne tient pas compte de l'influence de la direction
#  du vent et de la pression atmosphérique sur la force du vent et ne peut être utilisé que 
# pour des estimations grossières. Pour un calcul plus pré
