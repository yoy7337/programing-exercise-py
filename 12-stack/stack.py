class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# 使用範例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 輸出：3
print(stack.peek())  # 輸出：2
print(stack.size())  # 輸出：2