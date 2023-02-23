arr1 = [1,2,3,4,1235]
arr2 = [6,7,9,0]
arr3 = [1,11,61]

def contain_common(arr1, arr2):
    res = {}
    for i in arr1:
        if not res.get(i,0):
            res[i] = True
    for j in arr2:
        if res.get(j,0):
            return 'These two arrays have something in common'
        return 'Nothing in common'

print(contain_common(arr1,arr2))
print(contain_common(arr1,arr3))