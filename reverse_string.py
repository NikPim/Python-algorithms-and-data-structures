list_of_test = [["h","e","l","l","o"], [2], 'Hello World'] #if string is given as an array, than solution has O(1) extra memory

def reverse_string_1(string_1):
    if len(string_1) < 2 or not isinstance(string_1, list):
        return 'It won''t work'
    for i in range(len(string_1)//2):
        string_1[i], string_1[len(string_1) - 1 - i] = string_1[len(string_1) - 1 - i], string_1[i]
    return string_1

print(reverse_string_1(list_of_test[0]))
print(reverse_string_1(list_of_test[1]))
print(reverse_string_1(list_of_test[2]))
print('-------------')

list_of_test = [["h","e","l","l","o"], [2], 'Hello World'] #if string is given as a string

def reverse_string_2(string_2):
    if len(string_2) < 2 or not isinstance(string_2, str):
        return 'It won''t work'
    reversed_string = []
    for i in range(len(string_2) - 1, -1, -1):
        reversed_string.append(string_2[i])
    return ''.join(reversed_string)

print(reverse_string_2(list_of_test[0]))
print(reverse_string_2(list_of_test[1]))
print(reverse_string_2(list_of_test[2]))
print('-------------')

list_of_test = [["h","e","l","l","o"], [2], 'Hello World'] #pythonic way

def reverse_string_3(string_3):
    if len(string_3) > 1 and isinstance(string_3, list):
        string_3.reverse()
        return string_3
    elif len(string_3) > 1 and isinstance(string_3, str):
        string_3 = list(string_3)
        string_3.reverse()
        return ''.join(string_3)
    else:
        return 'It won''t work'

print(reverse_string_3(list_of_test[0]))
print(reverse_string_3(list_of_test[1]))
print(reverse_string_3(list_of_test[2]))