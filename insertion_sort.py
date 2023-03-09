df = [1,5,4,12,6,2,5,85,26,99,77,0]

def insertion_sort(data):
    for i in range(len(data)):
        if data[i] < data[0]:
            data.insert(0, data.pop(i))
        else:
            for j in range(1, i):
                if data[i] >= data[j-1] and data[i] < data[j]:
                    data.insert(j, data.pop(i))

insertion_sort(df)
print(df)