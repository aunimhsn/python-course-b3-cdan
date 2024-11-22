

phone_number:str = input('Veuillez entrer un numéro de téléphone à épeler : ')

digits_mapping:dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

result = ""

for digit in phone_number:
    # result += digits_mapping[digit].capitalize() + " "
    result += digits_mapping.get(digit, '[Character not mapped]') + " "

print(result.strip())