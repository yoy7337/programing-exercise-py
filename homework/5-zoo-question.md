# 動物園管理系統
## 題目描述
你將設計一個簡單的動物園管理系統，用來管理動物園中的動物。你需要創建類別來表示動物和動物園，並使用方法來添加動物、列出動物資訊、讓動物發出聲音等。具體要求如下：

1. 創建 Animal 類別(class)：
	- 每個動物有以下屬性(variable)：
		- name（名稱，例如 "Leo"）
		- species（種類，例如 "Dog"）
		- age（年齡，例如 3）
	- 創建一個 speak 方法(function)，根據動物的種類輸出不同的聲音：
		- "Dog" → "Woof!"
		- "Cat" → "Meow!"
		- "Bird" → "Chirp!"
		- 其他種類 → "Unknown sound."
2. 創建 Zoo 類別：
	- 這個類別有一個屬性 animals，它是一個列表（array），用來存放 Animal 的實例。
	- 創建以下方法：
		- add_animal：添加一個新的動物到動物園。
		- remove_animal：根據動物名稱移除動物。
		- list_animals：列出所有動物的名稱、種類和年齡。
		- make_all_speak：讓動物園中所有動物發出聲音。
3. 使用 loop：
	- 在 list_animals 和 make_all_speak 方法中，使用迴圈來遍歷動物列表。

4. 測試：
	- 創建一個 Zoo 實例。
	- 添加至少三隻動物（例如：Dog、Cat、Bird）。
	- 呼叫 list_animals 顯示所有動物資訊。
	- 呼叫 make_all_speak 讓所有動物發聲。
	- 移除一隻動物，然後再次呼叫 list_animals 確認移除成功。

### 輸出結果:
```text
Animal: Leo, Species: Dog, Age: 3
Animal: Mimi, Species: Cat, Age: 2
Animal: Tweety, Species: Bird, Age: 1
Leo says: Woof!
Mimi says: Meow!
Tweety says: Chirp!
After removing Mimi:
Animal: Leo, Species: Dog, Age: 3
Animal: Tweety, Species: Bird, Age: 1
```