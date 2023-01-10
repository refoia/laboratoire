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
