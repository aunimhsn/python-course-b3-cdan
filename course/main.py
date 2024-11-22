number = input("Entrer un nombre : ")
try:
    number = int(number)
    total = 10 / number
# ValueError sera levée si le casting n'est pas possible.
except ValueError:
    print("Vous n'avez pas entré un nombre...")
# ZeroDivisionError sera levée s'il y a une division par 0.
except ZeroDivisionError:
    print("La division par 0 est impossible...")
# Si aucune exception n'est levée, else sera exécuté.
else:
    print(f"Total : {total} - Tout s'est bien passé !")
# Erreur ou pas, finally sera exécuté.
finally:
    print("La gestion des erreurs / exceptions est terminée.")