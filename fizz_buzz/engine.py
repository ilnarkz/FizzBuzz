import argparse
from fizz_buzz.scripts.fizz_buzz import run


def main():
    parser = argparse.ArgumentParser(description='''FizzBuzz is a popular task
    given at job interviews. It displays numbers from 1 to 100. The program
    outputs the word "Fizz" instead of numbers divisible by three, and the word
    "Buzz" instead of numbers divisible by five. If the number is a multiple of
    both 3 and 5, the program prints the word "FizzBuzz".''')
    args = parser.parse_args()
    print('Welcome to Fizz Buzz!\nSubmit a number and get an answer!\nIf you '
          'want to exit, press "q".')
    print(run())


if __name__ == '__main__':
    main()
