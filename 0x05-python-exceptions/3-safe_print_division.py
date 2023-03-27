#!/usr/bin/python3

# safe_print_division : division two integer
# a : first number
# b : second number
# Return : integer or error

def safe_print_division(a, b):
    answer = 0
    try:
        answer = a / b
    except (TypeError, ZeroDivisionError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
        return (answer)
