import math

# Constantes
G = 6.674e-11  # Constante de gravitation universelle en N m^2/kg^2
M_EARTH = 5.972e24  # Masse de la Terre en kg
R_EARTH = 6371e3  # Rayon de la Terre en m

# Demande à l'utilisateur de saisir les caractéristiques des marées
amplitude = float(input("Entrez l'amplitude des marées en m: "))
period = float(input("Entrez la période des marées en jours: "))

# Calcule la vitesse de rotation de la Terre
omega = 2 * math.pi / (period * 24 * 3600)

# Calcule la force de marée
force = (G * M_EARTH * R_EARTH * amplitude * omega**2) / (2 * math.pi)

# Affiche le résultat
print("La force de marée est de", force, "N")


# Dans cet exemple, le programme demande à l'utilisateur de saisir l'amplitude et la période des marées et calcule la force de marée en utilisant la formule de marée de Harmonic (F = (GMdω^2)/(2π)). La force de marée est le vecteur de force qui décrit l'influence des marées sur un objet immergé dans l'océan.

# Il est important de noter que cet exemple ne tient pas compte de l'influence de la lune et du soleil sur les marées et ne peut être utilisé que pour des calculs de marée grossiers. Pour un calcul plus précis, vous


