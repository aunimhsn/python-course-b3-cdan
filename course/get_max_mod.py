def get_max(numbers:list[float]) -> float:
    if len(numbers) == 0:
        raise Exception('Liste vide, impossible de récupérer le maximum')
    
    result:float = numbers[0]

    for number in numbers:
        if result < number:
            result = number

    return result

print(get_max([1.5, 6, 5, 4]))
