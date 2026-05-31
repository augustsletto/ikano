def factorial(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        return f"type(n) should be int: type: {type(n)}"

    
    if n < 0:
        return False
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial("hej"))