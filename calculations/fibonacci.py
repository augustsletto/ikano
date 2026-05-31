def fibonacci(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    if n < 0:
        raise ValueError("n cannot be negative")
    a = 0
    b = 1
    for _ in range(n):
        temp = a + b
        a = b
        b = temp
    return a

# print(fibonacci(4.5))