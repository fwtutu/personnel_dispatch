# Personnel Dispatch System


## 環境安裝

### 前置需求
- Python 版本：3.x
- pip：請確保已安裝 Python 包管理器 pip
- MySQL 

### 安裝步驟

1. **克隆專案**
   ```bash
   git clone [<專案的Git倉庫網址>](https://github.com/fwtutu/personnel_dispatch.git)
   cd personnel_dispatch
    ```

2. **建立虛擬環境並安裝相依套件**
    ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
     ```

3. **設置 MySQL 資料庫**
設定 MySQL 資料庫並將以下配置放入 settings.py 文件中的 DATABASES 部分。

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dispatch_system',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    

4. **執行遷移**
    ```bash
    python manage.py migrate
    ```

5. **啟動伺服器**
    ```bash
    python manage.py runserver
    ```


## 版本更新


### 第一次更新 - 10/29: 登入系統
- 登入系統的基本功能，包括：
  - 使用者註冊
  - 使用者登入
  - 登入狀態管理
  - 提供錯誤訊息以增強使用者體驗  //待修改，massage問題一堆
  - SQL連接

### 第二次更新 - 10/30: 人員基本資料管理 - 管理員
- 人員基本資料管理功能，包括：
  - 更新基本資訊（姓名、年齡、聯絡資訊、地址）
  - 儲存功能
  - SQL連接

### 第三次更新 - 10/31: 個人資料維護 - 工作人員
- 人員個人資料維護功能，包括：
  - 更新基本資訊（姓名、年齡、聯絡資訊、地址）
  - 儲存功能
  - SQL連接

### 第四次更新 - 11/03: 簡易排班系統 - 排班、排班列表
- 人員個人資料維護功能，包括：
  - 更新基礎排班功能（人員、開始時間、結束時間、工時計算）
  - 儲存功能
  - SQL連接
  - 行事曆view
  - 限制個人排班
 

### 第五次更新 - 4/1: 客戶系統 + 預約照護系統

-   新增客戶資料管理功能，包括：
    -   客戶基本資料（姓名、聯絡方式、地址等）儲存與管理
    -   客戶資料查詢與更新功能

-   預約照護系統：
    -   客戶預約管理，包括預約時間、服務項目與負責人員的配對
    -   提供預約確認與取消功能
    -   系統自動將預約與員工排班進行匹配，並確保預約能成功成立
    -   提供預約記錄查看與修改功能


## 耽擱內容

- 提示訊息：找別的替代 massage
- URL 連接：按鈕、post 都還沒設，自己手動 call 網址

## 技術棧
- Django
- MySQL
- HTML
