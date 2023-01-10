import json

# Définissons une fonction qui vérifie si nous avons suffisamment de fonds pour effectuer une transaction
def check_funds(symbol, quantity, price, balance):
    total_cost = quantity * price
    if total_cost > balance:
        print("Fonds insuffisants pour effectuer la transaction.")
        return False
    return True

# Définissons une fonction qui met à jour notre solde après une transaction
def update_balance(symbol, quantity, price, balance, is_buy):
    total_cost = quantity * price
    if is_buy:
        balance -= total_cost
    else:
        balance += total_cost
    return balance

# Définissons une fonction qui effectue une transaction et enregistre les détails dans un fichier JSON
def trade(symbol, quantity, price, balance, is_buy):
    # Vérifions d'abord si nous avons suffisamment de fonds
    if not check_funds(symbol, quantity, price, balance):
        return

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
    with open("D:/laboratoire/code-php-openAI/txt/trades2.json", "a") as f:
        json.dump(trade_details, f)
        f.write("\n")

    # Mettez à jour notre solde
    balance = update_balance(symbol, quantity, price, balance, is_buy)
    return balance

# Testons notre fonction de trading en achetant 10 actions de la société XYZ au prix de 100 $ chacune avec un solde de 1000 $
balance = 1000
balance = trade("XYZ", 10, 100, balance, True)
print("Solde actuel : {}".format(balance))

# Testons notre fonction de trading en vendant 5 actions de la société XYZ au prix de 120 $ chacune
balance = trade("XYZ", 5, 120, balance, False)
print("Solde actuel : {}".format(balance))
