
# Création de la liste des opérations comptables
operations_comptables = []

# Ajout d'une opération de vente de produits pour un montant de 100 euros
operations_comptables.append(("vente", 100))

# Ajout d'une opération de paiement de frais de location pour un montant de 50 euros
operations_comptables.append(("frais de location", -50))

# Création de la liste des opérations bancaires
operations_bancaires = []

# Ajout d'une opération de virement bancaire pour un montant de 75 euros
operations_bancaires.append(("virement", 75))

# Ajout d'une opération de retrait en espèces pour un montant de 20 euros
operations_bancaires.append(("retrait", -20))

# Calcul du solde comptable en parcourant la liste des opérations comptables
solde_comptable = 0
for operation in operations_comptables:
    type_operation, montant = operation
    solde_comptable += montant

# Calcul du solde bancaire en parcourant la liste des opérations bancaires
solde_bancaire = 0
for operation in operations_bancaires:
    type_operation, montant = operation
    solde_bancaire += montant

# Affichage du solde final
print("Le solde comptable est de", solde_comptable, "euros.")
print("Le solde bancaire est de", solde_bancaire, "euros.")

# Vérification du rapprochement
if solde_comptable == solde_bancaire:
    print("Le rapprochement est correct.")
else:
    print("Le rapprochement est incorrect, il y a une écart de", solde_comptable - solde_bancaire, "euros.")

# Ce code crée deux listes d'opérations, une pour les opérations comptables et une pour les opérations bancaires, puis ajoute quelques opérations de test dans chaque liste. Il calcule ensuite le solde final de chaque liste en parcourant les opérations et en ajoutant chaque montant à une variable "solde". Enfin, il affiche les soldes comptable et bancaire et vérifie si le rapprochement est correct en comparant les deux soldes.

# Bien sûr, ce code ne constitue qu'un exemple simple et il pourrait être étendu et amélioré de nombreuses manières pour répondre à des besoins de comptabilité plus complexes.


