import heapq

# Constantes pour représenter les différentes parties de l'immeuble
FLOOR = "."
OBSTACLE = "X"
FIRE = "F"
PERSON = "P"
ESCAPE_LADDER = "E"

# Classe pour représenter un étage de l'immeuble
class Floor:
  def __init__(self, x, y, floor_type):
    self.x = x
    self.y = y
    self.floor_type = floor_type

# Classe pour représenter un noeud dans l'algorithme A*
class Node:
  def __init__(self, floor, g_score, f_score, prev):
    self.floor = floor
    self.g_score = g_score
    self.f_score = f_score
    self.prev = prev
  
  def __lt__(self, other):
    return self.f_score < other.f_score

# Fonction pour trouver le chemin le plus court entre deux étages
def find_path(floors, start, end):
  # Crée la liste ouverte et fermée
  open_list = []
  closed_list = set()
  
  # Ajoute le noeud de départ à la liste ouverte
  start_node = Node(start, 0, manhattan_distance(start, end), None)
  heapq.heappush(open_list, start_node)
  
  # Itère jusqu'à ce que la liste ouverte soit vide
  while open_list:
    # Prend le noeud avec la valeur f la plus basse
    current_node = heapq.heappop(open_list)
    current_floor = current_node.floor
    
    # Si on a atteint l'étage final, retourne le chemin
    if current_floor == end:
      path = []
      while current_node:
        path.append(current_node.floor)
        current_node = current_node.prev
      return path[::-1]
    
    # Ajoute l'étage courant à la liste fermée
    closed_list.add(current_floor)
    
    # Vérifie les étages adjacents
    for neighbor in get_adjacent_floors(floors, current_floor):
      # Ignore les étages déjà dans la liste fermée
      if neighbor in closed_list:
        continue
      
      # Calcul le coût de mouvement vers ce voisin
      g_score = current_node.g_score + manhattan_distance(current_floor, neighbor)
      
      # Vérifie si le voisin est déjà dans la liste ouverte
      neighbor_node = None
      for node in open_list:
        if node.floor == neighbor:
          neighbor_node = node
          break
      
      # Si le voisin est déjà dans la liste ouverte et que le coût de mouvement actuel est supérieur à celui du voisin, ignore le voisin
      if neighbor_node and g_score >= neighbor_node.g_score:
        continue
      
      # Ajoute le voisin à la liste ouverte avec le coût de mouvement et le coût total estimé
      f_score = g_score + manhattan_distance(neighbor, end)
      heapq.heappush(open_list, Node(neighbor, g_score, f_score, current_node))
  
  # Si on a parcouru toute la liste ouverte sans trouver de chemin, retourne None
  return None

# Fonction pour trouver les étages adjacents à un étage donné
def get_adjacent_floors(floors, floor):
  adjacents = []
  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    x = floor.x + dx
    y = floor.y + dy
    if x < 0 or y < 0 or x >= len(floors[0]) or y >= len(floors):
      continue
    if floors[y][x].floor_type == OBSTACLE or floors[y][x].floor_type == FIRE:
      continue
    adjacents.append(floors[y][x])
  return adjacents

# Fonction pour calculer la distance de Manhattan entre deux étages
def manhattan_distance(floor1, floor2):
  return abs(floor1.x - floor2.x) + abs(floor1.y - floor2.y)

  # Fonction pour charger le labyrinthe à partir d'un fichier
def load_maze(filename):
  floors = []
  people = []
  start = None
  end = None

  # Ouvre le fichier en mode lecture
  with open(filename, "r") as f:
    y = 0
    for line in f:
      x = 0
      row = []
      for c in line.strip():
        floor = Floor(x, y, c)
        row.append(floor)
        if c == PERSON:
          people.append(floor)
        elif c == START:
          start = floor
        elif c == END:
          end = floor
        x += 1
      floors.append(row)
      y += 1
  
  return floors, start, end, people 
# Teste la fonction pour trouver le chemin le plus court
floors, start, end, people = load_maze("D:/laboratoire/code-php-openAI/txt/maze.txt")
for person in people:
  path = find_path(floors, start, person)
  
  # Affiche le chemin trouvé
  if path:
    print(f"Found path to person at ({person.x}, {person.y})")
    for floor in path:
      print(f"({floor.x}, {floor.y})")
  else:
    print(f"No path found to person at ({person.x}, {person.y})")


  # Affiche le chemin trouvé
  if path:
    print(f"Found path to person at ({person.x}, {person.y})")
    for floor in path:
      print(f"({floor.x}, {floor.y})")
  else:
    print(f"No path found to person at ({person.x}, {person.y})")

# Trouve les trois solutions possibles pour sauver toutes les personnes
solutions = []
for i in range(len(people)):
  for j in range(i+1, len(people)):
    for k in range(j+1, len(people)):
      path1 = find_path(floors, start, people[i])
      path2 = find_path(floors, people[i], people[j])
      path3 = find_path(floors, people[j], people[k])
      path4 = find_path(floors, people[k], end)
      if path1 and path2 and path3 and path4:
        solutions.append([path1, path2, path3, path4])

# Affiche le nombre de solutions trouvées
print(f"Found {len(solutions)} solutions")

# Affiche les solutions trouvées
for solution in solutions:
  print("---")
  for path in solution:
    for floor in path:
      print(f"({floor.x}, {floor.y})")
