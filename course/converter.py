# Écrire un programme qui convertit en mph une vitesse donnée en km/h.
# Rappel : 1 mile = 1,609 km
# Bonus : Arrondir le résultat au centième près.


def converter(value_1):
  ''' fonction de conversion de km/h en mph'''
  value_2 = value_1 / 1.609
  return (f' {value_1} km/h = {format(value_2, '.02f')} mph')
                                         # {value_2:.2f}
# Demander à l'utilisateur une vitesse en km/h
user_entry = float(input('Veuillez entrer une vitesse en km/h : '))
print(converter(user_entry))
