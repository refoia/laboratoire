import chess
import chess.engine
import json

# Création d'un plateau d'échecs vide
board = chess.Board()

# Création d'un moteur d'échecs
engine = chess.engine.SimpleEngine.popen_uci("D:/lab/oratoire/cod/e-php-openAI/txt/best_move.json")

# Demande au moteur de trouver le meilleur coup pour le joueur blanc
result = engine.play(board, chess.engine.Limit(time=0.1))

# Enregistrement du meilleur coup dans un fichier JSON
best_move = result.move
data = {'best_move': str(best_move)}
with open('D:/laboratoire/code-php-openAI/txt/best_move.json', 'w') as outfile:
    json.dump(data, outfile)

# Fermeture du moteur d'échecs
engine.quit()
