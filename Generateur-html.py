

# Importe les modules nécessaires
from IPython.display import display, HTML

# Crée le début de la page HTML
html = '<html><head><style>'

# Ajoute du CSS pour styliser les tableaux et la card
html += 'table { border-collapse: collapse; }'
html += 'table, th, td { border: 1px solid black; padding: 5px; }'
html += '.card { box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; border-radius: 5px; }'
html += '.card:hover { box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); }'
html += '.card-container { display: flex; }'
html += '.card-left { flex: 1; padding: 10px; }'
html += '.card-right { flex: 1; padding: 10px; }'

# Ferme la balise de style et ajoute le titre de la page
html += '</style></head><body><h1>Mes tableaux et ma card</h1>'

# Crée le premier tableau
html += '<table><tr><th>Colonne 1</th><th>Colonne 2</th></tr>'
html += '<tr><td>Ligne 1, colonne 1</td><td>Ligne 1, colonne 2</td></tr>'
html += '<tr><td>Ligne 2, colonne 1</td><td>Ligne 2, colonne 2</td></tr></table>'

# Crée le deuxième tableau
html += '<table><tr><th>Colonne 1</th><th>Colonne 2</th></tr>'
html += '<tr><td>Ligne 1, colonne 1</td><td>Ligne 1, colonne 2</td></tr>'
html += '<tr><td>Ligne 2, colonne 1</td><td>Ligne 2, colonne 2</td></tr></table>'

# Crée la card
html += '<div class="card-container"><div class="card-left">'
html += '<div class="card"><p>Contenu de la card</p></div></div>'
html += '<div class="card-right"><p>Autre contenu</p></div></div>'

# Ferme la page HTML
html += '</body></html>'

# Affiche la page HTML
display(HTML(html))


# Ce code va générer une page HTML qui affiche deux tableaux et une card avec du contenu et du CSS pour les styliser. Vous pouvez ajouter ou modifier le contenu et le CSS selon vos besoins.
















