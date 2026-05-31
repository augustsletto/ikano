def fibonacci(n: int) -> int:
    try:
        n = int(n)
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
    except TypeError as e:
        return str(e)
# print(fibonacci(4.5))