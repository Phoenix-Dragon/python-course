# L’utilisateur entre un nombre. Le programme stock
# les 10 premiers résultats de la table de
# multiplication choisie par l’utilisateur dans une
# liste puis affiche cette liste.
# BONUS
# Signaler au passage, à l’aide d’une astérisque,
# ceux qui sont des multiples de 3.

def multiplication(value):
  list_multiplication = []
  list_multiplication_3 = []
  for i in range(11):
    list_multiplication.append(value * i)
  for j in range(11):
    if list_multiplication[j] % 3 == 0:
      list_multiplication_3.append(f'{list_multiplication[j]}*')
    else :
      list_multiplication_3.append(list_multiplication[j])
  return list_multiplication, list_multiplication_3

user_entry = int(input('Quelle table voulez vous afficher : '))
print(multiplication(user_entry))