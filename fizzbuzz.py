a = int(input('Enter number between 1 & 100: '))

for fizzbuzz in range(1, a+1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('fizzbuzz')
    elif fizzbuzz % 3 == 0:
        print('fizz')
    elif fizzbuzz % 5 == 0:
        print('buzz')
    else:
        print (fizzbuzz)