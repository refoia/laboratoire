html = """
<html>
  <head>
    <style>
      /* Mise en forme de la card */
      .card {
        background-color: lightgrey;
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
      }

      /* Mise en forme des tableaux */
      table {
        border-collapse: collapse;
      }
      td, th {
        border: 1px solid black;
        padding: 5px;
      }
      th {
        background-color: lightgrey;
      }
    </style>
  </head>
  <body>
    <!-- Première card -->
    <div class="card">
      <h2>Titre de la card</h2>
      <p>Contenu de la card</p>
    </div>

    <!-- Premier tableau -->
    <table>
      <tr>
        <th>Colonne 1</th>
        <th>Colonne 2</th>
      </tr>
      <tr>
        <td>Ligne 1, colonne 1</td>
        <td>Ligne 1, colonne 2</td>
      </tr>
      <tr>
        <td>Ligne 2, colonne 1</td>
        <td>Ligne 2, colonne 2</td>
      </tr>
    </table>

    <!-- Deuxième tableau -->
    <table>
      <tr>
        <th>Colonne 1</th>
        <th>Colonne 2</th>
      </tr>
      <tr>
        <td>Ligne 1, colonne 1</td>
        <td>Ligne 1, colonne 2</td>
      </tr>
      <tr>
        <td>Ligne 2, colonne 1</td>
        <td>Ligne 2, colonne 2</td>
      </tr>
    </table>
  </body>
</html>
"""

# Enregistrement de la page HTML dans un fichier
with open("D:/laboratoire/code-php-openAI/txt/page3.html", "w") as f:
  f.write(html)

# Ce code crée une page HTML avec une "card" en haut de la page, suivie de deux tableaux. La mise en forme de la card et des tableaux est définie dans une feuille de style en-tête de la page. Lorsque vous ouvrez le fichier "page.html" dans un navigateur, vous devriez voir la page avec la card et les deux tableaux.

# Notez que ce code est un exemple simple pour illustrer comment créer une page HTML avec du CSS en utilisant Python. Il existe de nombreuses autres façons de faire cela, et vous pouvez facilement ajouter d'autres éléments et styles à votre page HTML si vous le souhaitez.
