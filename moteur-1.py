import requests

def search(query):
  api_key = "YOUR_API_KEY"
  cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
  query = query.replace(" ", "+")
  url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
  response = requests.get(url)
  results = response.json()
  return results["items"]

query = input("Entrez votre requête de recherche: ")
results = search(query)

for result in results:
  print(result["title"])
  print(result["link"])
  print()


# Pour utiliser ce code, vous devez d'abord obtenir une clé API et un ID de moteur de recherche personnalisé auprès de Google. Vous pouvez vous inscrire à l'API de recherche Google ici: https://developers.google.com/custom-search/v1/overview

# Une fois que vous avez obtenu votre clé API et votre ID de moteur de recherche personnalisé, remplacez les chaînes "YOUR_API_KEY" et "YOUR_CUSTOM_SEARCH_ENGINE_ID" par ces valeurs dans le code ci-dessus.


# Ce code effectue une requête à l'API de recherche Google en utilisant la requête de l'utilisateur, puis imprime les titres et les liens des premiers résultats de recherche. Vous pouvez personnaliser ce code en fonction de vos besoins, par exemple en affichant plus d'informations sur chaque résultat ou en ajoutant des options de filtrage ou de tri.



# Import des bibliothèques nécessaires
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Création d'un circuit quantique avec un qubit et un bit classique
q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

# Appliquer une porte X (NOT) sur le qubit
qc.x(q[0])

# Mesurer le qubit et enregistrer le résultat dans le bit classique
qc.measure(q, c)

# Exécution du circuit sur un simulateur local
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1)
result = job.result()

# Affichage du résultat de la mesure
print(result.get_counts(qc))

# Ce code crée un circuit quantique avec un qubit et un bit classique, applique une porte X (NOT) sur le qubit, mesure le qubit et affiche le résultat de la mesure.

# Il est important de noter que ce code ne fonctionnera que si vous avez installé la bibliothèque Qiskit et les dépendances nécessaires. Si vous rencontrez des problèmes ou si vous avez des questions sur son utilisation, n'hésitez pas à me poser d'autres questions.
























