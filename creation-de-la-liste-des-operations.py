# Création de la liste des opérations
operations = []

# Ajout d'une opération de vente de produits pour un montant de 100 euros
operations.append(("vente", 100))

# Ajout d'une opération de paiement de frais de location pour un montant de 50 euros
operations.append(("frais de location", -50))

# Calcul du solde en parcourant la liste des opérations
solde = 0
for operation in operations:
    type_operation, montant = operation
    solde += montant

# Affichage du solde final
print("Le solde final est de", solde, "euros.")

#Ce code crée une liste d'opérations, ajoute deux opérations
#  (une vente et un paiement de frais de location) à la liste,
#  puis parcourt la liste pour calculer le solde final en ajoutant 
# chaque montant à la variable "solde". Enfin, 
# le solde final est affiché à l'écran.

#Bien sûr, ce code ne constitue qu'un exemple simple
#  et il pourrait être étendu et amélioré de nombreuses
#  manières pour répondre à des besoins de comptabilité plus complexes.