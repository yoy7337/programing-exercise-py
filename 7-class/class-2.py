class Car:
    # 類別屬性
    wheels = 4
    
    def __init__(self, brand):
        # 實例屬性
        self.brand = brand

# 創建物件
car1 = Car("Toyota")
car2 = Car("Honda")

# 訪問屬性
print(car1.brand)    # 輸出: Toyota
print(car2.brand)    # 輸出: Honda
print(car1.wheels)   # 輸出: 4
print(car2.wheels)   # 輸出: 4

# 修改類別屬性
Car.wheels = 6
print(car1.wheels)   # 輸出: 6
print(car2.wheels)   # 輸出: 6

# 修改單一物件的屬性
car1.brand = "BMW"
print(car1.brand)    # 輸出: BMW
print(car2.brand)    # 輸出: Honda