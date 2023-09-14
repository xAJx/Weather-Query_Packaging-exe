# 台灣地圖_各縣市_天氣查詢_PyQt5、打包exe

## 採用的天氣網址是 https://weather.com/zh-TW/weather/today/該縣市專屬的代碼 [在code裡面名為 loc]
-----------------------------------------------------
### 1.由於採用這個網站，一開始需要知道每個縣市的專屬代碼 
<br/>

### 2.在code 裡面 用 group 方法，讓 checkbox 一次只能選擇一個選項查詢
<br/> 

### 3. 設計 兩種 結果_ 一個是 五個 checkbox欄位 都要打勾_才有結果、另一個是 一次只能選擇 一個 GUI地圖 左側欄位的 checkbox

------------------------------------------------------
#### I. 打包 exe 指令: pyinstaller -F weather.ui -o storeui.py --noconsole (-F 雜檔包一起、weather.ui 為Qt 的 檔名、storeui.py 為自己命名存放轉檔後的位置名稱、--noconsole 讓背景黑色的 cmd 執行視窗 不要跳出 [在spec檔 裡也可以把 console 改 False])

#### II. 設計把 png、jpg、gif 檔，包進py檔裡面，但目前只能在本機端執行


