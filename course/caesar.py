# Écrire la fonction qui permet de réaliser le chiffre de César
# avec un décalage de 1 dans un premier temps.
# Dans un second temps, ajouter le décalage en paramètre
# de la fonction.

def encryption_caesar(msg:str, offset:int=1) -> str:
    result = ""
    for char in msg :
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            position = ord(char) - base
            new_position = (position + offset) % 26
            new_char = chr(base + new_position)
            result += new_char
        else:
            result += char
    return result

def decryption_caesar(msg:str, offset:int=1) -> str:
    result = ""
    for char in msg :
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            position = ord(char) - base
            new_position = (position - offset) % 26
            new_char = chr(base + new_position)
            result += new_char
        else:
            result += char
    return result

print(encryption_caesar(input(f'Entrez votre message'), int(input(f"Entrez une clé numérique : "))))
print(decryption_caesar(input(f'Entrez votre message'), int(input(f"Entrez la clé numérique de déchiffrage : "))))

