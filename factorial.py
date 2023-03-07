def iterative_factorial(value):
    f = 1
    for i in range(2, value+1):
        f*=i
    return f

def recursive_factorial(value):
    if value == 2:
        return 2
    return value * recursive_factorial(value-1)

print(iterative_factorial(5))
print(recursive_factorial(5))