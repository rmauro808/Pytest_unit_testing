def add(num1, num2):
    return num1 + num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    if num2 == 0:
        raise ValueError
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2
