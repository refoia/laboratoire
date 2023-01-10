import random

# Constantes pour représenter les différentes parties du labyrinthe
EMPTY = " "
WALL = "|"
START = "S"
END = "E"

# Génère aléatoirement un labyrinthe de dimensions width x height
def generate_maze(width, height):
  # Crée une grille vide de taille width x height
  maze = []
  for i in range(height):
    maze.append([EMPTY] * width)

  # Place les murs du labyrinthe
  for i in range(height):
    for j in range(width):
      if i % 2 == 0 or j % 2 == 0:
        maze[i][j] = WALL

  # Place le point de départ et d'arrivée
  start_x = random.randint(1, width-2)
  start_y = random.randint(1, height-2)
  end_x = random.randint(1, width-2)
  end_y = random.randint(1, height-2)
  maze[start_y][start_x] = START
  maze[end_y][end_x] = END

  return maze, start_x, start_y, end_x, end_y

# Affiche le labyrinthe sous forme de grille
def print_maze(maze):
  for row in maze:
    print("".join(row))

# Teste le générateur de labyrinthe
maze, start_x, start_y, end_x, end_y = generate_maze(10, 10)
print_maze(maze)
print(f"Start: ({start_x}, {start_y})")
print(f"End: ({end_x}, {end_y})")
 



def intelT():
    
  # Teste le générateur de labyrinthe
  maze, start_x, start_y, end_x, end_y = generate_maze(10, 10)
  print_maze(maze)
  print(f"Start: ({start_x}, {start_y})")
  print(f"End: ({end_x}, {end_y})")
  

intelT() 