# Écrire un programme qui créera une nouvelle liste
# en filtrant les doublons

def lookalike(tab):
  tab_result = []
  for i in range(len(tab)):
    if tab[i] not in tab_result:
      tab_result.append(tab[i])
  return tab_result



user_entry = [1, 4, 3, 5, 6, 6, 7, 7, 4, 3, 8, 9, 12, 56]
print(lookalike(user_entry))