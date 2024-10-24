warreHouse_1 =  ["pomme", "banane", "orange", "poire", "raisin"]
warreHouse_2 =  ["orange", "ananas", "banane", "pêche", "kiwi"]

#Trouver l'intersection
intersection = list(set(warreHouse_1) & set(warreHouse_2))  

print(intersection)

#Trouver l'union
union = list(set(warreHouse_1) | set(warreHouse_2))   

print(union)

# Trouver les articles uniquement dans warreHouse_1
uniques_warreHouse_1 = list(set(warreHouse_1) - set(warreHouse_2))  
print(uniques_warreHouse_1)

# Fusionner les articles des deux listes
fusion = list(set(warreHouse_1) | set(warreHouse_2))  
print(fusion)







