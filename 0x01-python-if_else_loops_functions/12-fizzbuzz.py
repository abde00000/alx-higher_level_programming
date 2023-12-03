#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number = 'fizzBuzz'
        elif number % 3 == 0:
            number = 'FIZZ'
        elif number % 5 == 0:
            number = 'BUZZ'
print("{}".format(number), end=' ')
