import chess
import chess.engine

# Création d'un moteur d'IA avec Stockfish
engine = chess.engine.SimpleEngine.popen_uci("stockfish")

# Création d'un plateau d'échecs
board = chess.Board()

# Boucle principale du jeu
while not board.is_game_over():
  # Si c'est au tour des blancs de jouer, demander à l'utilisateur de saisir son coup
  if board.turn:
    move = input("Entrez votre coup (exemple : e2e4): ")
    board.push_san(move)
  # Sinon, c'est au tour des noirs, donc faire jouer l'IA
  else:
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
  print(board)

# Afficher le résultat final
result = board.result()
if result == "1-0":
  print("Les blancs ont gagné !")
elif result == "0-1":
  print("Les noirs ont gagné !")
else:
  print("Partie nulle.")

# Fermer le moteur d'IA
engine.close()

# Classe représentant une case du plateau d'échecs
class Square:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.piece = None
  
  def __str__(self):
    return f"({self.x}, {self.y})"

# Classe représentant une pièce d'échecs
class Piece:
  def __init__(self, color, type, square):
    self.color = color
    self.type = type
    self.square = square
    self.square.piece = self
  
  def move(self, square):
    self.square.piece = None
    self.square = square
    self.square.piece = self

# Classe représentant un plateau d'échecs
class Board:
  def __init__(self):
    self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
    self.pieces = []
  
  def add_piece(self, piece, square):
    self.pieces.append(piece)
    piece.square = square
    square.piece = piece
  
  def move_piece(self, piece, square):
    if piece.square == square:
      return False
    if not self.is_valid_move(piece, square):
      return False
    piece.move(square)
    return True
   
def is_valid_move(self, piece, square):
  # Vérifie que la pièce ne dépasse pas les limites du plateau
  if square.x < 0 or square.x > 7 or square.y < 0 or square.y > 7:
    return False
  
  # Vérifie que la pièce ne se déplace pas sur une case occupée par une pièce de la même couleur
  if square.piece is not None and square.piece.color == piece.color:
    return False
  
  # Implémentation spécifique aux différentes pièces
  if piece.type == "pawn":
    return self.is_valid_move_pawn(piece, square)
  elif piece.type == "rook":
    return self.is_valid_move_rook(piece, square)
  elif piece.type == "knight":
    return self.is_valid_move_knight(piece, square)
  elif piece.type == "bishop":
    return self.is_valid_move_bishop(piece, square)
  elif piece.type == "queen":
    return self.is_valid_move_queen(piece, square)
  elif piece.type == "king":
    return self.is_valid_move_king(piece, square)
  else:
    return False



def is_valid_move_queen(self, piece, square):
    return self.is_valid_move_bishop(piece, square) or self.is_valid_move_rook(piece, square)
  
def is_valid_move_king(self, piece, square):
    dx = abs(piece.square.x - square.x)
    dy = abs(piece.square.y - square.y)
    return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)
  
def get_piece_at(self, x, y):
    return self.squares[x][y].piece

# Création d'un plateau d'échecs et ajout de quelques pièces
board = Board()
board.add_piece(Piece("white", "pawn", board.squares[1][1]), board.squares[1][1])
board.add_piece(Piece("black", "pawn", board.squares[6][6]), board.squares[6][6])
board.add_piece(Piece("white", "rook", board.squares[0][0]), board.squares[0][0])
board.add_piece(Piece("black", "knight", board.squares[7][1]), board.squares[7][1])
board.add_piece(Piece("white", "bishop", board.squares[0][2]), board.squares[0][2])
board.add_piece(Piece("black", "queen", board.squares[7][3]), board.squares[7][3])
board.add_piece(Piece("white", "king", board.squares[0][4]), board.squares[0][4])

# Déplacement d'une pièce
board.move_piece(board.get_piece_at(1, 1), board.squares[2][1])
board.move_piece(board.get_piece_at(7, 1), board.squares[5][2])
board.move_piece(board.get_piece_at(0, 4), board.squares[1][3])
board.move_piece(board.get_piece_at(7, 3), board.squares[5][3])

