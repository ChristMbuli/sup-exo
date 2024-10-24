chaine = "python est amusant"

frequence = {}
for letter  in chaine:
    if letter != " ":
        frequence[letter] = frequence.get(letter, 0) + 1

print("Fréquence des lettres: ", frequence)