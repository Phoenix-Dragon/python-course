import random

# Écrire le code du jeu du shifumi, l’utilisateur joue contre l’ordinateur 
# qui choisira aléatoirement entre la pierre, la feuille ou les ciseaux.
# La partie se joue en deux manches gagnantes.

## Attention ce code ne fonctionne pas !!

def game():
  ''' fonction du jeu shifumi '''
  movements = ["pierre", "feuille", "ciseaux"]
  machine_score = 0
  player_score = 0
  while machine_score < 3 and player_score < 3:
    machine_number = random.randint(0, 2)
    machine_move = movements[machine_number]
    player_move = input("Entrez pierre / feuille / ciseaux : ").lower 
    if machine_move == "pierre" and player_move == "pierre":
      print(f'Egalité')
    elif machine_move == "pierre" and player_move == "feuille":
      print(f'+1 pour joueur')
      player_score += 1
    elif machine_move == "pierre" and player_move == "ciseaux":
      print (f'+1 pour l\'ordinateur')
      machine_score += 1
    elif machine_move == "feuille" and player_move == "pierre":
      print (f'+1 pour l\'ordinateur')
      machine_score += 1
    elif machine_move == "feuille" and player_move == "feuille":
      print(f'Egalité')
    elif machine_move == "feuille" and player_move == "ciseaux":
      print(f'+1 pour joueur')
      player_score += 1
    elif machine_move == "ciseaux" and player_move == "pierre":
      print(f'+1 pour joueur')
      player_score += 1
    elif machine_move == "ciseaux" and player_move == "feuille":
      print (f'+1 pour l\'ordinateur')
      machine_score += 1
    elif machine_move == "ciseaux" and player_move == "ciseaux":
      print(f'Egalité')
  if player_score == 3:
    return (f'Victoire du joueur')
  else :
    return (f'Victoire de l\'ordinateur')
      

print(game())