# 什麼是鏈結串列？
鏈結串列是一種線性資料結構，由一系列節點（Node）組成，每個節點包含兩部分：

## 資料（Data）：儲存實際的值。
下一個節點的參考（Next）：指向串列中的下一個節點。
與陣列（例如 Python 的 list）不同，鏈結串列的節點在記憶體中不一定是連續儲存的，這使得插入和刪除操作更靈活，但隨機存取效率較低。

## 鏈結串列的種類
單向鏈結串列（Singly Linked List）：每個節點只指向下一個節點。
雙向鏈結串列（Doubly Linked List）：每個節點指向下一個和上一個節點。
循環鏈結串列（Circular Linked List）：最後一個節點指向第一個節點，形成一個循環。
Python 實作範例（單向鏈結串列）
Python 本身沒有內建的鏈結串列資料結構，但可以通過自定義類來實現。以下是一個簡單的單向鏈結串列實作：

```py
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
```

## 主要操作
1. 插入：
頭部插入：O(1)
尾部插入：O(n)
特定位置插入：O(n)
2. 刪除：
頭部刪除：O(1)
尾部或特定位置刪除：O(n)
3. 遍歷：O(n)
4. 搜尋：O(n)
### 優點
動態大小：可以輕鬆擴展或縮減。
插入和刪除效率高（特別是在頭部）。
適合需要頻繁插入/刪除的場景。
### 缺點
隨機存取效率低（無法像陣列使用索引直接存取）。
額外的記憶體開銷（儲存指向下一個節點的參考）。
不適合需要快速搜尋的場景。
### 應用場景
實現堆疊（Stack）和佇列（Queue）。
瀏覽器的前進/後退功能（雙向鏈結串列）。
圖形演算法中的鄰接表表示。

