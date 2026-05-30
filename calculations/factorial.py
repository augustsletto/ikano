def factorial(n):
    try:
        int(n)
    except ValueError:
        return "Not an integer, try again."
    
    if n < 0:
        return False
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(50))