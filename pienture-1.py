import tkinter as tk
import random

# Fonction pour générer une couleur aléatoire
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)

# Création de la fenêtre et du canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=800, bg='white')
canvas.pack()

# Fonction pour dessiner un cercle aléatoire lorsque la souris est cliquée
def draw_circle(event):
    x, y = event.x, event.y
    radius = random.randint(5, 50)
    color = get_random_color()
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline=color)

# Liaison de la fonction à l'événement "clic de souris"
canvas.bind("<Button-1>", draw_circle)

# Affichage de la fenêtre
window.mainloop()


# Ce code crée une fenêtre avec un canvas, définit une fonction pour dessiner un cercle aléatoire lorsque la souris est cliquée et lie cette fonction à l'événement "clic de souris". Chaque fois que vous cliquerez sur le canvas, un cercle de couleur aléatoire et de taille aléatoire sera dessiné à l'emplacement du clic.

# Il est important de noter que ce code ne fonctionnera que si vous avez installé la bibliothèque Tkinter et les dépendances nécessaires. Si vous rencontrez des problèmes ou si vous avez des questions sur son utilisation, n'hésitez pas à me poser d'autres questions.





