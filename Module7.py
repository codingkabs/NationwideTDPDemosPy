import math
import Module6 as m6
m6.hello()

from Module6 import hello as h
h()


def hello():
    print("Hello World")
    print("Hello World")


# x = 1
# while x < 10:
#     hello()
#     x += 1


def hello_params(name):
    print(f"Hello {name}")

# hello_params("John")
# hello_params("Jordan")
# hello_params("James")

def hello_return_method():
    return "Hello World"

# my_function = hello_return_method()
# print(my_function)

def add_two_numbers(a, b):
    result = a + b
    return result

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# result = add_two_numbers(num1, num2)
# print(result)

def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
    print("Done!")


def countdown_rec(n):
    if n == -1:
        print("Done!")
    else:
        print(n)
        countdown_rec(n - 1)

countdown(5)
countdown_rec(5)