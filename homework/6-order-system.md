# 餐廳點餐系統
## 題目描述
你將設計一個餐廳點餐系統，讓顧客可以瀏覽菜單並點餐。這個系統需要管理菜單項目並計算訂單總價。具體要求如下：

1. 創建 Dish 類別(class)：
	- 每道菜有以下屬性(variable)：
		- name（名稱，例如 "Pizza"）
		- price（價格，例如 10.5）
	- 使用 __init__ 方法初始化這些屬性。
2. 創建 Restaurant 類別：
	- 這個類別有一個屬性 menu，它是一個列表（array），用來存放 Dish 的實例。
	- 創建以下方法(function)：
		- add_dish：添加一道新菜到菜單。
		- show_menu：顯示菜單上所有菜的名稱和價格。
		- take_order：接受顧客的點餐（一個菜名列表），計算並返回總價。如果某道菜不在菜單上，輸出提示訊息。
3. 使用 loop：
	- 在 show_menu 中使用迴圈顯示每道菜。
	- 在 take_order 中使用迴圈處理顧客的點餐列表。
4. 測試要求：
	- 創建一個 Restaurant 實例。
	- 添加至少四道菜到菜單（例如：Pizza、Burger、Salad、Soda）。
	- 呼叫 show_menu 顯示菜單。
	- 模擬顧客點餐（例如：["Pizza", "Soda", "Cake"]），輸出總價並處理不在菜單上的菜。

## 範例輸出
```
Menu:
1. Pizza - $10.5
2. Burger - $8.0
3. Salad - $6.5
4. Soda - $2.0
Order: ['Pizza', 'Soda', 'Cake']
Cake is not on the menu!
Total price: $12.5
```