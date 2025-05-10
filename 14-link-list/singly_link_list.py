# 定義節點類
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 定義鏈結串列類
class LinkedList:
    def __init__(self):
        self.head = None
    
    # 在串列末尾添加節點
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # 列印串列
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 使用範例
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 輸出: 1 -> 2 -> 3 -> None