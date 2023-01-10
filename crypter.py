# Importe les modules nécessaires
from Crypto.Cipher import AES
import base64

# Demande à l'utilisateur de saisir le message et la clé de chiffrement
message = input("Entrez le message à crypter: ")
key = input("Entrez la clé de chiffrement (16, 24 ou 32 caractères): ")

# Ajoute des caractères de remplissage au message pour qu'il ait une longueur multiple de 16 (taille du bloc AES)
message = message + " " * (16 - (len(message) % 16))

# Crée un objet de type AES en mode CTR
cipher = AES.new(key, AES.MODE_CTR)

# Chiffre le message et encode-le en base64
encrypted_message = base64.b64encode(cipher.encrypt(message.encode()))

# Affiche le message chiffré
print("Message chiffré:", encrypted_message)

# Demande à l'utilisateur de saisir la clé de déchiffrement
key = input("Entrez la clé de déchiffrement: ")

# Crée un nouvel objet de type AES en mode CTR avec la clé de déchiffrement
cipher = AES.new(key, AES.MODE_CTR)

# Décode le message chiffré de base64 et le déchiffre
decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message)).decode().strip()

# Affiche le message déchiffré
print("Message déchiffré:", decrypted_message)


# Voici un exemple de code Python qui utilise la bibliothèque "pycryptodome" pour crypter et décrypter un message en utilisant l'algorithme de chiffrement AES (Advanced Encryption Standard):
