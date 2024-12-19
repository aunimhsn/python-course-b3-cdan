
def fizz_buzz(limit:int) -> None:
    if limit == 0:
        raise Exception('La limite doit être plus grande que 0')

    for i in range(1, limit+1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(16)
