from string import ascii_lowercase

text = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth."
text = text.lower()

result:dict = {}

# alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in ascii_lowercase:
    result[letter] = text.count(letter)

print(result)

