# 父類別
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "I can speak!"

# 子類別
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

    def purr(self):
        return f"{self.name} is purring..."

# 創建物件
cat = Cat("Whiskers")

# 使用方法
print(cat.speak())    # 輸出: Whiskers says meow!
print(cat.purr())     # 輸出: Whiskers is purring...