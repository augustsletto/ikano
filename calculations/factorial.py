def factorial(n: int) -> int:
    try:
        int(n)
    except ValueError:
        return "not an int"
    
    if n < 0:
        return False
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial("hej"))