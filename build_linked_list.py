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

    def insert(self, index, value):
        new_node = NewNode(value, None)
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            current_node = self.traverse_to_index(index-1)

            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.traverse_to_index(index-1)
            current_node.next = current_node.next.next
        self.length -= 1

    def traverse_to_index(self, index):
        current_node = self.head
        i = 0
        while i != index:
            current_node = current_node.next
            i+=1
        return current_node

    def print_val(self):
        current = self.head
        while current:
            print(current.value, "\b--->", end="")
            current = current.next
        print()


linked_list = LinkedList(10)
linked_list.prepend(16)
linked_list.append(7)
linked_list.append(12)
linked_list.append(17)
linked_list.append(19)

# print('16 --> 10 --> 7')
# print(linked_list.head.value)
# print(linked_list.head)
# print(linked_list.head.next)
# print(linked_list.head.next.value)
# print(linked_list.head.next)
# print(linked_list.head.next.next)
# print(linked_list.head.next.next.value)
# print(linked_list.head.next.next)
# print(linked_list.head.next.next.next)
# print(linked_list.tail.value)
# print(linked_list.tail)
# print(linked_list.tail.next)
linked_list.print_val()
linked_list.insert(2,121)
linked_list.print_val()
linked_list.remove(6)
linked_list.print_val()
print(linked_list.length)