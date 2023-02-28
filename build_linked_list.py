class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value, None, None)
        self.length = 1
        self.tail = self.head
    
    def append(self, value):
        new_node = Node(value, None, self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, self.head, None)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value, None, None)
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            if index <= self.length // 2:
                current_node = self.traverse_to_index(index-1)
            else:
                current_node = self.reverse_to_index(index-1)
            
            next_node = current_node.next
            next_node.prev = new_node
            new_node.prev = current_node
            new_node.next = next_node
            current_node.next = new_node
            self.length += 1
    
    def remove(self, index):
        if index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        elif index == self.length - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            if index <= self.length // 2:
                current_node = self.traverse_to_index(index)
            else:
                current_node = self.reverse_to_index(index+1)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        self.length -= 1

    def traverse_to_index(self, index):
        current_node = self.head
        i = 0
        while i != index:
            current_node = current_node.next
            i+=1
        return current_node
    
    def reverse_to_index(self, index):
        current_node = self.tail
        i = self.length - 1
        while i != index:
            current_node = current_node.prev
            i-=1
        return current_node

    def print_val(self):
        current = self.head
        while current:
            print(current.value, "\b--->", end="")
            current = current.next
        print()

    def print_reversed(self):
        current = self.tail
        while current:
            print(current.value, "\b--->", end="")
            current = current.prev
        print()

    def reverse_singly(self):
        first = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        print(self.head.value)


linked_list = DoublyLinkedList(10)
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
# print(linked_list.length)

# linked_list.print_val()
# linked_list.insert(2,121)
# linked_list.print_val()
# #linked_list.remove(6)
# linked_list.print_val()
# print(linked_list.length)
# linked_list.print_reversed()
# linked_list.remove(4)
# linked_list.print_reversed()
# linked_list.print_val()
# print(linked_list.length)
# linked_list.insert(6,93)
# print(linked_list.length)
# linked_list.print_val()
# print(linked_list.length)
# linked_list.remove(6)
# linked_list.print_val()
# linked_list.print_reversed()
# linked_list.remove(0)
# linked_list.print_val()
# linked_list.print_reversed()
linked_list.print_val()
linked_list.reverse_singly()
linked_list.print_val()



