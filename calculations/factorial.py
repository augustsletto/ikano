def factorial(n: int) -> int:

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")

    
    if n < 0:
        raise ValueError("n cannot be negative")
    if n == 0:
        return 1
    
    r = 1
    for num in range(2, n + 1):
        r *= num
    return r

# print(factorial(1000))