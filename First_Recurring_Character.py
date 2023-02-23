array = [1,2,5,5,2,1,7,7,1]
array2 = [1,2,3,4,6,7]
array3 = [1]

def first_recurring(array):
    res = {}
    for ind, val in enumerate(array):
        if res.get(val,0):
            return val
        else:
            res[val] = ind
    return -1

print(first_recurring(array))
print(first_recurring(array2))
print(first_recurring(array3))