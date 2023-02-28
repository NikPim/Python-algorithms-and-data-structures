class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def push(self, value):
        new_node = Node(value, None)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp
        self.length += 1

    def peek(self):
        if self.length == 0:
            return None
        return self.top.value
    
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1

    def is_empty(self):
        return self.bottom == None
    
my_stack = Stack()
my_stack.push('Google')
my_stack.push('Youtube')
my_stack.push('Discord')
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.is_empty())
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
print(my_stack.is_empty())
