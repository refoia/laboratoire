import socket

# Création d'un socket pour écouter les requêtes entrantes
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080)) # Bind le socket à l'adresse locale et au port 8080
server_socket.listen(1) # Écoute les requêtes entrantes

print('Serveur web en écoute sur le port 8080...')

while True:
    # Attend une requête entrante
    client_socket, client_address = server_socket.accept()

    # Récupère la requête HTTP envoyée par le client
    request = client_socket.recv(1024)

    # Affiche la requête HTTP dans la console
    print('Requête reçue : \n', request)

    # Création de la réponse HTTP à envoyer au client
    response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!'

    # Envoie la réponse HTTP au client
    client_socket.sendall(response)

    # Ferme la connexion avec le client
    client_socket.close()
