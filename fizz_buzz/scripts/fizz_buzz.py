def print_value(number):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz!')
    elif number % 3 == 0:
        print('Fizz!')
    elif number % 5 == 0:
        print('Buzz!')
    else:
        print(number)


def run():
    while True:
        char = input('Number: ')
        if char == 'Q' or char == 'q':
            break
        elif not char.isdigit():
            print('Please, input the number!')
            continue
        number = int(char)
        print_value(number)
