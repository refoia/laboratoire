import json

def trade(symbol, quantity, price):
    # Effectuez une transaction ici en utilisant l'API de votre plateforme de trading
    # ...

    # Enregistrez les détails de la transaction dans un dictionnaire
    trade_details = {
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "timestamp": "2022-12-18T12:34:56Z"  # Utilisez la date et l'heure courantes
    }

    # Écrivez les détails de la transaction dans un fichier JSON
    with open("D:/laboratoire/code-php-openAI/txt/trades.json", "a") as f:
        json.dump(trade_details, f)
        f.write("\n")

# Testons notre fonction de trading en achetant 10 actions de la société XYZ au prix de 100 $ chacune
trade("XYZ", 10, 100)

# Voici un exemple de code Python qui peut être utilisé pour créer un bot de trading
#  qui enregistre les transactions dans un fichier JSON :

# Notez que ce code est un exemple simplifié et
#  qu'il y a de nombreux autres éléments à prendre en compte lors de
#   la création d'un bot de trading, tels que la gestion des erreurs,
#    la gestion des fonds et la stratégie de trading elle-même.
#     Il est recommandé de bien comprendre 
# ces éléments avant de créer un bot de trading en utilisant des fonds réels.