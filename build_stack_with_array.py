class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, value):
        self.array.append(value)

    def peek(self):
        if len(self.array) == 0:
            return None
        return self.array[len(self.array) - 1]
    
    def pop(self):
        self.array.pop()

    def is_empty(self):
        return self.array == None
    
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
