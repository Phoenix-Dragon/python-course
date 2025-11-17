# Ecrire un programme qui demande à l'utilisateur les longueurs des cotés d'un triangle 
# et qui indique si ce triangle est équilatéral, isocèle ou quelconque

def triangle(side_1, side_2, side_3):
  if side_1 == side_2 == side_3:
    return (f'Ce triangle est équilatéral de longueur {side_1} unités.')
  elif (side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3):
    return (f'Ce triangle est isocèle.')
  else :
    return (f'Ce triangle est quelconque.')

value_1 = int(input('Entrez la longueur du première côté : '))
value_2 = int(input('Entrez la longueur du deuxième côté : '))
value_3 = int(input('Entrez la longueur du troisième côté : '))
print("")
print(triangle(value_1, value_2, value_3))
