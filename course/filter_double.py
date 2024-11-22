# Solution 1
# numbers = [8, 7, 11, 7, 2, 10, 5, 8]
# result = []

# for number in numbers:
#     if number not in result:
#         result.append(number)

# print(result)

# Solution 2
numbers = [8, 7, 11, 7, 2, 10, 5, 8]
result = list(set(numbers))
print(result)
