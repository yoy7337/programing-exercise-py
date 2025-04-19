# programing-exercise-py


## 開發環境
mac os <br>
安裝軟體
1. [Visual Studio CODE](https://code.visualstudio.com/): 程式開發編輯器，下載後安裝使用
2. [Homebrew](https://brew.sh/): Mac 的套件管理工具，依照上面的提示打開 Mac 終端機後輸入指令
3. Python 3.12+: Python 穩定版本(2025/2/4)，打開終端機輸入以下指令即可安裝
```
brew install python@3.12
```
4. [iTerm](https://iterm2.com/): 比較好用的 mac 終端機工具，下載後安裝使用

## 執行程式方式
打開終端機
```
python3 [檔案路徑].py
```

---

## Python 虛擬環境
Python 虛擬環境是一個獨立的 Python 執行環境，允許你為不同的專案安裝和管理獨立的套件及其版本，而不會與系統的 Python 環境或其他專案的套件發生衝突。每個虛擬環境都有自己的 Python 執行檔和 site-packages 目錄，與其他環境隔離。


### 為什麼需要虛擬環境？
1. 隔離專案依賴：不同專案可能需要不同版本的同一套件（如 Django 1.x vs Django 2.x），虛擬環境確保每個專案的依賴獨立。
2. 避免衝突：防止套件版本或依賴之間的兼容性問題。
3. 系統環境乾淨：避免在全局 Python 環境中安裝大量套件，保持系統環境整潔。
4. 便於部署：虛擬環境中的依賴可以輕鬆導出（如 requirements.txt），便於在其他環境中重現。
5. 測試與開發：可以在不同環境中測試不同版本的套件，無需影響主系統。

### 建立 Python 虛擬環境的步驟
1. 檢查 Python 是否安裝： 確保系統已安裝 Python（建議 3.x 版本）。在終端機輸入：
```sh
python --version
python3 --version
```

2. 建立虛擬環境： 使用 venv 模組在指定目錄中建立虛擬環境。例如，建立一個名為 myenv 的虛擬環境：
```sh
python -m venv myenv
```
   - myenv 是虛擬環境的目錄名稱，可自訂。
   - 執行後，會在當前目錄下生成一個 myenv 資料夾，包含虛擬環境的檔案。

3. 啟用虛擬環境：
```sh
source myenv/bin/activate
```

4. 驗證虛擬環境
```sh
python --version
pip --version
```

5. 安裝套件： 在虛擬環境中，使用 pip 安裝專案所需的套件。例如：
```sh
pip install requests
```

6. 退出虛擬環境：
```sh
deactivate
```