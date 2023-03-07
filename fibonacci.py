def iterative_fibonacci(value):
    a = 0
    b = 1
    for i in range(value-1):
        s = a + b
        a = b
        b = s
    return s

def recursive_fibonacci(value):
    if value < 2:
        return value
    return recursive_fibonacci(value-1) + recursive_fibonacci(value-2)

print(iterative_fibonacci(12))
print(recursive_fibonacci(12))