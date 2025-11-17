oceans = [
    "Pacific",
    "Atlantic",
    "Indian",
    "Southern",
    "Arctic"
]

with open("./data/oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
 # Autre possibilité
 # print(ocean, file=f)
