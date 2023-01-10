

from cryptography.fernet import Fernet

def generate_key():
  """
  Cette fonction génère une clé de chiffrement AES aléatoire.
  """
  return Fernet.generate_key()

def save_key(key, key_file):
  """
  Cette fonction enregistre la clé de chiffrement AES dans un fichier.
  """
  with open(key_file, "wb") as f:
    f.write(key)

def load_key(key_file):
  """
  Cette fonction charge une clé de chiffrement AES à partir d'un fichier.
  """
  with open(key_file, "rb") as f:
    return f.read()

def encrypt(message, key):
  """
  Cette fonction chiffre un message en utilisant la clé de chiffrement AES spécifiée.
  """
  f = Fernet(key)
  return f.encrypt(message)

def decrypt(encrypted_message, key):
  """
  Cette fonction déchiffre un message chiffré en utilisant la clé de chiffrement AES spécifiée.
  """
  f = Fernet(key)
  return f.decrypt(encrypted_message)


# Pour utiliser ces fonctions, vous pouvez par exemple faire quelque chose comme ceci :


# Génération de la clé de chiffrement
key = generate_key()

# Enregistrement de la clé dans un fichier
save_key(key, "D:/laboratoire/code-php-openAI/key.bin")

# Chargement de la clé à partir du fichier
key = load_key("D:/laboratoire/code-php-openAI/key.bin")

# Chiffrement d'un message
encrypted_message = encrypt("Mon message secret", key)

# Déchiffrement du message chiffré
decrypted_message = decrypt(encrypted_message, key)

print(decrypted_message)  # Affiche "Mon message secret"

# Note : cet exemple utilise 
# le mode de chiffrement AES en mode
#  de chiffrement de bloc (CBC).
#  Pour utiliser un autre mode 
# de chiffrement, vous pouvez 
# utiliser la classe AESCipher
#  du module
#  cryptography.hazmat.primitives.ciphers.
import os
from cryptography.fernet import Fernet

class Cipher:
    """
    Cette classe permet de chiffrer et de déchiffrer des messages en utilisant la bibliothèque de chiffrement Fernet.
    """

    KEY_FILE = "key.bin"
    MESSAGE_FILE = "message.txt"

    def __init__(self):
        """
        Initialise un nouvel objet Cipher.
        """
        self.key = None

    def generate_key(self):
        """
        Génère une clé de chiffrement AES aléatoire et la stocke dans l'objet Cipher.
        """
        self.key = Fernet.generate_key()

    def save_key(self):
        """
        Enregistre la clé de chiffrement AES dans un fichier.
        """
        if self.key is None:
            raise ValueError("Aucune clé n'a été générée.")

        with open(self.KEY_FILE, "wb") as f:
            f.write(self.key)

    def load_key(self):
        """
        Charge une clé de chiffrement AES à partir d'un fichier et la stocke dans l'objet Cipher.
        """
        if not os.path.exists(self.KEY_FILE):
            raise FileNotFoundError("Le fichier de clé n'existe pas.")

        with open(self.KEY_FILE, "rb") as f:
            self.key = f.read()

    def encrypt(self, message):
        """
        Chiffre un message en utilisant la clé de chiffrement AES de l'objet Cipher.
        """
        if self.key is None:
            raise ValueError("Aucune clé n'a été chargée.")

        f = Fernet(self.key)
        return f.encrypt(

