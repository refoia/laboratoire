class Character:
    """
    Cette classe représente un personnage dans le jeu de rôle.
    """
    def __init__(self, name, level, race, job, health, mana):
        self.name = name
        self.level = level
        self.race = race
        self.job = job
        self.health = health
        self.mana = mana

    def attack(self, target):
        """
        Cette méthode permet au personnage d'attaquer une cible.
        """
        # On calcule les dégâts infligés en fonction du niveau du personnage
        damage = self.level * 10
        # On enlève les dégâts à la vie de la cible
        target.health -= damage
        print(f"{self.name} attaque {target.name} et inflige {damage} points de dégâts")

class Monster:
    """
    Cette classe représente un monstre dans le jeu de rôle.
    """
    def __init__(self, name, level, health, damage):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage

    def attack(self, target):
        """
        Cette méthode permet au monstre d'attaquer une cible.
        """
        # On enlève les dégâts à la vie de la cible
        target.health -= self.damage
        print(f"{self.name} attaque {target.name} et inflige {self.damage} points de dégâts")

# Création du personnage du joueur
player = Character("Bob", 1, "humain", "guerrier", 100, 50)

# Création du monstre
monster = Monster("Goblin", 1, 50, 20)

# Le joueur attaque le monstre
player.attack(monster)

# Le monstre attaque le joueur
monster.attack(player)
