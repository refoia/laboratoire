
# Définir les variables de départ
taille_tournesol = 0  # Taille du tournesol, en cm
vitesse_croissance = 5  # Vitesse de croissance du tournesol, en cm/jour
jours_depuis_semis = 0  # Nombre de jours écoulés depuis le semis

# Boucle infinie qui simule la croissance du tournesol
while True:
  # Incrémenter le nombre de jours écoulés
  jours_depuis_semis += 1
  # Incrémenter la taille du tournesol en fonction de la vitesse de croissance
  taille_tournesol += vitesse_croissance
  # Afficher l'état du tournesol
  print(f"Jour {jours_depuis_semis}: le tournesol mesure {taille_tournesol} cm.")
  
  # Si le tournesol atteint une taille de 100 cm, arrêter la boucle
  if taille_tournesol >= 100:
    break
