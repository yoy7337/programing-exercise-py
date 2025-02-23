class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    # 計算是否及格
    def is_passing(self):
        return self.grade >= 60
    
    # 更新成績
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"{self.name}'s grade updated to {self.grade}"

# 創建物件
student = Student("Alice", 75)

# 使用方法
print(student.is_passing())        # 輸出: True
print(student.update_grade(85))    # 輸出: Alice's grade updated to 85
print(student.is_passing())        # 輸出: True