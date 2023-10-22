def get_factorial(n):
    factor = 1
    while n > 1:
        factor *= n
        n -= 1
    return factor


print(get_factorial(6))