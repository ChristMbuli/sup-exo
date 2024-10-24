notes = {"Alice":15, "Bob":12,"Claire":17, "David":9, "Emma":18}

#Ajouter un nouvel étudiant 
notes["Frank"] = 17
print(notes)

#Modifier la note de Bob
notes["Bob"] = 16
print(notes)

#supprimer David
del notes["David"]
print(notes)

# Afficher la moyenne de la classe
moyenne = sum(notes.values()) / len(notes)
print("Moyenne de la classe:", moyenne)
