def fibonacci(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        return f"type(n) should be int: type: {type(n)}"
    
    if n < 0:
        return False
    a = 0
    b = 1
    for _ in range(n):
        temp = a + b
        a = b
        b = temp
    return a
        
print(fibonacci(4.5))