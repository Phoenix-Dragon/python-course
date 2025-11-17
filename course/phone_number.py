# Écrire un programme qui épellera un numéro de
# téléphone en toute lettre.

# Correction #####################################"
phone_number = input(f"Veuillez saisir un numéro de téléphone : ")

digit_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
}

result = " "
for digit in phone_number :
    result += digit_mapping.get(digit, "[character not mapped]") + " "
    #result += digit_mapping[digit] + " "

result = result.strip()
print(result)