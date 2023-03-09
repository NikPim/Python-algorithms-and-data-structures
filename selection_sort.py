df = [1,5,4,12,6,2,5,85,26,99,77,0]

def selection_sort(data):
    min_index = 0
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


selection_sort(df)
print(df)