# 1. Calculer une réduction de 15% des prix de la liste suivante
# INPUT : prices = ['95,62€', '11,61€', '100,50€', '62,33€']
# OUTPUT : prices_discounted ...

def reduction(prices:list[str], number_reduction:int) ->list[float]:
    prices_discounted = []
    for price in prices:
        price_without_euro = price.replace('€', '')
        price_with_point = price_without_euro.replace(',', '.')
        price_with_float = float(price_with_point)
        price_with_reduction = round(price_with_float * number_reduction, 2)
        prices_discounted.append(str(price_with_reduction).replace('.', ',') + "€")
    return prices_discounted

# Exemple
prices = ['95,62€', '11,61€', '100,50€', '62,33€']
print(reduction(prices, 0.85))



# 2. Extraire le nom et le prénom de chacun des mails suivants
# INPUT : emails = ['pierre.dupont@yahoo.fr', 'marie.curie@gmail.com']
# OUTPUT : 
# users = [
#     {
#         'first_name': 'pierre', 
#         'last_name': 'dupont'
#     },
#     {
#         'first_name': 'marie', 
#         'last_name': 'curie'
#     },
# ]

def dictionnarisation(emails: list[str]) -> list[dict]:
    users = []
    for email in emails:
        user = {}
        email_before_at = email.split('@')[0]
        first_and_last_name = email_before_at.split('.')
        user['first_name'], user['last_name'] = first_and_last_name[0], first_and_last_name[1]
        users.append(user)
    return users

# Exemple
emails = ['pierre.dupont@yahoo.fr', 'marie.curie@gmail.com']
print(dictionnarisation(emails))

# 3. Supprimer de la liste les fruits qui finit par une voyelle
# INPUT : fruits = ['Apple', 'Cherry', 'Mandarin', 'Banana', 'Pear']
# OUTPUT : fruits = ['Mandarin', 'Pear']

def end_with_consonant(fruits:list[str]) -> list[str]:
    fruits_end_with_consonant = []
    vowels = ['aeiouyAEIOUY']
    for fruit in fruits:
        if fruit[-1] not in vowels:
            fruits_end_with_consonant.append(fruit)
    return fruits_end_with_consonant

# Exemple
fruits = ['Apple', 'Cherry', 'Mandarin', 'Banana', 'Pear']
print(end_with_consonant(fruits))

# 4. Faire une fonction appelée "words_count" qui compte les mots d'un texte en entrée
# INPUT : sentence = "J'adore la langage de programmation Python"
# OUTPUT : 7

def words_count(sentence:str) -> int:
    count = 0
    sentence_without_space = sentence.replace("'", ' ').split(' ')
    for word in sentence_without_space:
        count += 1
    return count

# Exemple
sentence = "J'adore la langage de programmation Python"
print(words_count(sentence))

# 5. Faire une fonction appelée "get_largest_gap"
# qui retourne l'écart entre la note la plus basse et la meilleure note
# INPUT : marks = [8, 17.5, 6, 11, 15]
# OUTPUT : 11.5   (17.5 - 6)

def get_largest_gap(marks:list[float]) -> int:
    return max(marks) - min(marks)

# Exemple
marks = [8, 17.5, 6, 11, 15]
print(get_largest_gap(marks))

# 6. Faire une fonction appelée "get_ages_average" 
# qui calcule la moyenne d'âges des utilisateurs.
# INPUT : 
# users = [
#     {
#         'first_name': 'pierre', 
#         'last_name': 'dupont',
#         'age': 42
#     },    
#     {
#         'first_name': 'marie', 
#         'last_name': 'curie',
#         'age': 18
#     },
#     {
#         'first_name': 'marie', 
#         'last_name': 'curie',
#         'age': 35
#     },
# ]
# OUTPUT : ages_average = 71.67   ((42+18+35) / 3)

def get_ages_average(users:list[dict]) -> float:
    sum_of_ages = 0
    count = 0
    for user in users:
        sum_of_ages += user['age']
        count += 1
    return round(sum_of_ages/count, 2)



# Exemple
users = [
    {
        'first_name': 'pierre', 
        'last_name': 'dupont',
        'age': 42
    },    
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 18
    },
    {
        'first_name': 'marie', 
        'last_name': 'curie',
        'age': 35
    },
]
print(get_ages_average(users))