

# I. Acquisition des notes
marks = []

while True:
    mark = input("Enter a mark  (or a negative number to exit)) :")

    try:
        mark_float = float(mark)
    except ValueError:
        print('Vous n\'avez saisi un nombre...')
    else:
        if mark_float < 0:
            break
        else:
            marks.append(mark_float)

print(f'Il y a {len(marks)} notes')     

# II. Calcul de la moyenne
try:
    average = sum(marks) / len(marks)
except ZeroDivisionError:
    print('Il n\'y a pas de note... calcul de la moyenne impossible...')
else:
    print(f'La moyenne des notes est : {average:.2f}')