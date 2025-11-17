# A l'aide de vos recherches, écrire une fonction
# permettant de générer une couleur [RGB] aléatoire.
# BONUS
# Écrire une seconde fonction s'appuyant sur la première,
# celle-ci permettra d'écrire un message d'une couleur
# aléatoire dans la console.
from random import randint
from sty import fg

def generate_rgb() -> tuple[int]:
    red, green, blue =randint(0, 255), randint(0, 255), randint(0, 255)
    return red, green, blue

def generate_foreground_color_1(red, green, blue):
    return fg(red, green, blue)

color_1 = generate_foreground_color_1(*generate_rgb())
red, green, blue = generate_rgb()
color_2 =generate_foreground_color_1(red, green, blue) 

print(color_1, "hello", fg.rs)
print(color_2, "hello", fg.rs)
