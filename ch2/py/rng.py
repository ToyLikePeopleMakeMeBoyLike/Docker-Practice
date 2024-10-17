from random import randint

min_number = int(input('enter min num: '))
max_number = int(input('enter max num: '))

if (max_number < min_number):
    print('invalid - shutting down')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)