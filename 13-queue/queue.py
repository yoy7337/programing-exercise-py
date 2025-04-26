class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity  # Initialize fixed-size array
        self.front = 0  # Index of the front element
        self.rear = -1  # Index of the last element
        self.length = 0   # Current number of elements

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full, cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.items[self.rear] = item
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.length -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]
    
    def is_empty(self):
        return self.length == 0
    
    def is_full(self):
        return self.length == self.capacity

    def size(self):
        return self.length

# 使用範例
queue = Queue(5)  # Create a queue with capacity 5
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 輸出：1
print(queue.peek())    # 輸出：2
print(queue.size())    # 輸出：2