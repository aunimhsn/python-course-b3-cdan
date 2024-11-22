from random import randint

difficulty = input('1. Facile (0-10) - 2. Moyen (0-100) - 3. Difficile (0-1000) : ')

while difficulty not in ['1', '2', '3']:
    difficulty = input('1. Facile (0-10) - 2. Moyen (0-100) - 3. Difficile (0-1000) : ')

maximum = 100
if difficulty == '1':
    maximum = 10
elif difficulty == '2':
    maximum = 100
elif difficulty == '3':
    maximum = 1000
else:
    maximum = 100

secret = randint(0, maximum)
user_number = int(input(f'Veuillez entrer un nombre entre 0 et {maximum} : '))
attempts = 1

while user_number != secret:
    if secret > user_number:
        print('C\'est plus grand')
    else:
        print('C\'est plus petit')

    user_number = int(input(f'Veuillez entrer un nombre entre 0 et {maximum} : '))
    attempts += 1

print(f'Bravo, vous avez trouvé le nombre secret {secret} en {attempts} essai.s')