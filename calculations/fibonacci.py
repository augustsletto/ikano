def fibonacci(n):
    try:
        int(n)
    except ValueError:
        return "Not an integer, try again."
    
    if n < 0:
        return False
    a = 0
    b = 1
    for _ in range(n):
        temp = a + b
        a = b
        b = temp
    return a
        
print(fibonacci(10))