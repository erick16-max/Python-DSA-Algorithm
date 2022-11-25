#stack algorithmn to for Last in First out(LIFO)
class Stack:
    def __init__(self):
        self.stack = list()
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        return self.stack.append(item)
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None
    def the_stack(self):
        return self.stack

new_stack = Stack()
new_stack.push(2)
new_stack.push(3)
print(new_stack.pop())