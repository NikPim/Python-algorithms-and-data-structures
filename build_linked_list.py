class NewNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = NewNode(value, None)
        self.length = 1
        self.tail = self.head
    
    def append(self, value):
        new_node = NewNode(value, None)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        self.head = NewNode(value, self.head)
        self.length += 1

    def print_val(self):
        current = self.head
        while current:
            print(current.value, "\b--->", end="")
            current = current.next
        print()


linked_list = LinkedList(10)
# print('10 --> None')
# print(linked_list.head.value)
# print(linked_list.tail.value)
# print('10 --> 7')
# print(linked_list.head.value)
# print(linked_list.tail.value)
linked_list.prepend(16)
# print('16 --> 10 --> 7')
# print(linked_list.head.value)
# print(linked_list.head.next.value)
# print(linked_list.tail.value)
linked_list.append(7)

print('16 --> 10 --> None')
print(linked_list.head.value)
print(linked_list.head)
print(linked_list.head.next)
print(linked_list.tail.value)
print(linked_list.tail)
print(linked_list.tail.next)

print('16 --> 10 --> 7')
print(linked_list.head.value)
print(linked_list.head)
print(linked_list.head.next)
print(linked_list.head.next.value)
print(linked_list.head.next)
print(linked_list.head.next.next)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next)
print(linked_list.head.next.next.next)
print(linked_list.tail.value)
print(linked_list.tail)
print(linked_list.tail.next)

linked_list.print_val()