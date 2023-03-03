def factorial(x):
    if isinstance(x, int):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    else:
        raise TypeError("Input argument must be an integer.")


print(factorial(4.5))
