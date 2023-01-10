import heapq

# Constantes pour représenter les différentes parties de l'immeuble
FLOOR = "."
WALL = "|"
FIRE = "F"
PERSON = "P"
LADDER = "L"

# Représente une position dans l'immeuble
class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self.x, self.y))

  def __repr__(self):
    return f"({self.x}, {self.y})"

# Représente une case de l'immeuble
class Square:
  def __init__(self, position, square_type):
    self.position = position
    self.square_type = square_type
    self.visited = False

# Représente l'immeuble
class Building:
  def __init__(self, width, height, fire_floor):
    self.width = width
    self.height = height
    self.fire_floor = fire_floor
    self.squares = []
    self.start = None
    self.end = None
    self.people = []
    self.ladders = []

  # Ajoute une case à l'immeuble
  def add_square(self, position, square_type):
    square = Square(position, square_type)
    self.squares.append(square)
    if square_type == LADDER:
      self.ladders.append(position)
    elif square_type == PERSON:
      self.people.append(position)

  # Définit la position de départ du pompier
  def set_start(self, position):
    self.start = position

  # Définit la position d'arrivée du pompier (extérieur de l'immeuble)
  def set_end(self, position):
    self.end = position

# Représente une action que le pompier peut effectuer (se déplacer d'une case)
class Action:
  def __init__(self, cost, position):
    self.cost = cost
    self.position = position

# Représente un noeud de l'arbre de recherche (position du pompier et coût total pour y arriver)
class Node:
  def __init__(self, position, cost, previous_node):
    self.position = position
    self.cost = cost
    self.previous_node = previous_node

  # Compare deux noeuds en f
