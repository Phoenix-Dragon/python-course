import random 

# Entrer un nombre entre 0 et 100 : 70
# Le nombre est plus grand que 70
# Entrer un nombre entre 0 et 100 : 88
# Le nombre est plus petit que 88
# Entrer un nombre entre 0 et 100 : 84
# Le nombre est plus grand que 84
# Entrer un nombre entre 0 et 100 : 85
# Bravo, vous avez trouvé en 4 essais

def game(difficulty):
  ''' fonction du jeu Plus ou Moins'''
  search = -1
  counter = 0
  if difficulty == "facile" or difficulty == "1":
    maximum = 10
  elif difficulty == "moyen" or difficulty == "2":
    maximum = 100
  elif difficulty == "difficile" or difficulty == "3":
    maximum = 1000
  else :
    return (f'Revenez quand vous aurez appris à écrire !')
  value = random.randint(0, maximum)
  while value != search:
    search = int(input('Entrez un nombre : '))
    counter +=1
    if value < search:
      print (f'Le nombre est plus petit')
    elif value > search:
      print(f'Le nombre est plus grand')
    else :
      return (f'Bravo, vous avez gagné. Essayez un niveau plus difficile. \n Vous avez réussi en {counter} essais.')
  
user_entry = input('Entrez votre difficulté ( 1 - Facile (0-10), 2 - Moyen (0-100), 3 - Difficile (0-1000)) : ').lower()
print(game(user_entry))
