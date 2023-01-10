import random

def main():
  # On définit les différentes options possibles
  options = ['pierre', 'feuille', 'ciseaux']

  # On demande à l'utilisateur de choisir une option
  user_choice = input('Choisissez une option parmi pierre, feuille ou ciseaux : ')

  # On vérifie que l'option choisie par l'utilisateur est valide
  if user_choice not in options:
    print('Option non valide, veuillez réessayer')
    return

  # On fait choisir une option au hasard à l'ordinateur
  computer_choice = random.choice(options)

  # On affiche les choix de l'utilisateur et de l'ordinateur
  print(f'Vous avez choisi {user_choice} et l\'ordinateur a choisi {computer_choice}')

  # On détermine le résultat du jeu en fonction des choix
  if user_choice == computer_choice:
    print('Egalité')
  elif (user_choice == 'pierre' and computer_choice == 'ciseaux') or (user_choice == 'feuille' and computer_choice == 'pierre') or (user_choice == 'ciseaux' and computer_choice == 'feuille'):
    print('Vous avez gagné')
  else:
    print('L\'ordinateur a gagné')

if __name__ == '__main__':
  main()
