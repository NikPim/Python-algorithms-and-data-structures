df = [1,5,4,12,6,2,5,85,26,99,77,0]

def bubble_sort(data):
    for i in range(len(data)-1):
        counter = 0
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                counter +=1
        if counter == 0:
            return
        
bubble_sort(df)
print(df)