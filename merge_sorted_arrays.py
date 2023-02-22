def merge(arr_1, arr_2):
    if not arr_1:
        return arr_2
    elif not arr_2:
        return arr_1
    merged_arr = []
    i = 0
    j = 0
    while (i < len(arr_1) and j < len(arr_2)):
        print(arr_1[i], arr_2[j])
        if arr_1[i] < arr_2[j]:
            merged_arr.append(arr_1[i])
            i+=1
        else:
            merged_arr.append(arr_2[j])
            j+=1
        print(merged_arr)
    return merged_arr + arr_1[i:] + arr_2[j:]

arr_1 = [1,2,7,12,54]
arr_2 = [2,4,5,11,78]
print(merge(arr_1,arr_2))

arr_1 = []
arr_2 = [2,4,5,11,78]
print(merge(arr_1,arr_2))