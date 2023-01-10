# Définition de la classe Noeud
class Noeud:
  def __init__(self, valeur, gauche=None, droite=None):
    self.valeur = valeur
    self.gauche = gauche
    self.droite = droite

# Création de l'arbre de probabilité
arbre = Noeud(0.7, Noeud(0.2), Noeud(0.1, Noeud(0.4), Noeud(0.6)))
