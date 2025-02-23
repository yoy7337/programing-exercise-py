# 定義一個類別
class Dog:
    # 類別屬性（所有物件共享）
    species = "Canis familiaris"
    
    # 初始化方法（建構子）
    def __init__(self, name, age):
        # 實例屬性（每個物件獨立）
        self.name = name
        self.age = age
    
    # 定義一個方法
    def bark(self):
        return f"{self.name} says woof!"

# 創建物件
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# 訪問屬性與方法
print(dog1.name)         # 輸出: Buddy
print(dog2.age)          # 輸出: 5
print(dog1.bark())       # 輸出: Buddy says woof!
print(dog1.species)      # 輸出: Canis familiaris