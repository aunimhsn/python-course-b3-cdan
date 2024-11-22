table = int(input('Quelle table voulez-vous afficher ? '))
result = []

for i in range(1, 11):
    if (table * i) % 3 == 0:
        result.append(f'{table * i}*')
    else:  
        result.append(table * i)

print(result)