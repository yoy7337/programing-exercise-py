def factorial(n):
    if n == 0 or n == 1:  # 基本情況
        return 1
    else:
        return n * factorial(n - 1)  # 遞迴情況

# 測試
print(factorial(5))  # 輸出: 120 (5! = 5 × 4 × 3 × 2 × 1)