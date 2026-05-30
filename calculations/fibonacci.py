def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        temp = a + b
        a = b
        b = temp
    return a
        
        
print(fibonacci(10))