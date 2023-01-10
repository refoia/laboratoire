

def solve(grid):
  """
  Cette fonction résout un Sudoku en utilisant une approche récursive.
  """
  # On cherche une case vide (0) dans la grille
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        # On essaie chaque nombre possible (de 1 à 9)
        for number in range(1, 10):
          if is_valid(grid, i, j, number):
            # On met le nombre dans la case et on continue à résoudre la grille
            grid[i][j] = number
            if solve(grid):
              return True
            # Si la grille n'est pas valide, on réinitialise la case à 0
            grid[i][j] = 0
        # Si aucun nombre ne convient, on retourne False pour remonter dans l'appel récursif
        return False
  # Si la grille est complète, on retourne True
  return True

def is_valid(grid, row, col, number):
  """
  Cette fonction vérifie si un nombre peut être mis dans une case de la grille sans violer les règles du Sudoku.
  """
  # On vérifie si le nombre apparaît déjà dans la ligne ou la colonne
  for i in range(9):
    if grid[row][i] == number or grid[i][col] == number:
      return False

  # On vérifie si le nombre apparaît déjà dans le carré 3x3
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if grid[start_row + i][start_col + j] == number:
        return False
  # Si aucune vérification n'a échoué, on retourne True
  return True

grid = [   [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8,]] 
