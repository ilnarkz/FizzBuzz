# FizzBuzz

[![Maintainability](https://api.codeclimate.com/v1/badges/0ae19d477a89c7631e92/maintainability)](https://codeclimate.com/github/ilnarkz/FizzBuzz/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/0ae19d477a89c7631e92/test_coverage)](https://codeclimate.com/github/ilnarkz/FizzBuzz/test_coverage) [![fizz_buzz](https://github.com/ilnarkz/FizzBuzz/actions/workflows/ci.yml/badge.svg)](https://github.com/ilnarkz/FizzBuzz/actions/workflows/ci.yml)

FizzBuzz is a popular task given at job interviews. It displays numbers from 1 to 100. The program outputs the word
"Fizz" instead of numbers divisible by three, and the word "Buzz" instead of numbers divisible by five. If the number
is a multiple of both 3 and 5, the program prints the word "FizzBuzz".

## 1. Installation

### 1.1 Cloning the repository and installing dependencies

```bash
git clone https://github.com/ilnarkz/FizzBuzz
cd FizzBuzz
```

Installing dependencies (you need use **Poetry**)

```bash
make install
```

### 1.2 Activate virtual environment

```bash
python3 -m venv <name of the created environment>
source  <name of the created environment>/bin/activate
```


## 2. Running a CLI

To start the CLI, use

```bash
fizz_buzz
```

To start the help, use 

```bash
fizz_buzz -h
```
