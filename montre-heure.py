
import tkinter as tk
import time

# Création de la fenêtre principale
root = tk.Tk()
root.title("Montre")

# Création de l'étiquette qui affiche l'heure
label = tk.Label(root, font=("Arial", 50))
label.pack()

# Fonction qui met à jour l'heure affichée
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

# Mise à jour de l'heure toutes les secondes
update_time()

# Exécution de la boucle principale de l'interface graphique
root.mainloop()
