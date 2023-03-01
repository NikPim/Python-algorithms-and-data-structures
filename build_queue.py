class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.length == 0:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value, None)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        temp = self.first
        self.first = temp.next
        self.length -= 1


queue = Queue()

queue.enqueue(3)
print(queue.first)
print(queue.first.next)
print(queue.last)
print(queue.last.next)
queue.enqueue(5)
print('_____')
print(queue.first)
print(queue.first.next)
print(queue.last)
print(queue.last.next)
queue.enqueue(7)
print('_____')
print(queue.first)
print(queue.first.next)
print(queue.last)
print(queue.last.next)

