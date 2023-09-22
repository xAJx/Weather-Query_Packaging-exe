# *PyQt5*、*打包exe* _台灣地圖 _各縣市_ 天氣查詢 

> ## 採用的天氣網址是 *https://weather.com/zh-TW/weather/today/該縣市專屬的代碼* [在code裡面名為 loc]
-----------------------------------------------------
### 1.由於採用這個網站，一開始*需要知道每個縣市的專屬代碼* 
<br/>

### 2.用 _group 方式_，讓 checkbox _一次只能選擇一個選項_ 查詢
<br/> 

### 3. 設計 *兩種 結果*_ 一個是 五個 checkbox欄位 都要打勾_才有結果、另一個是 一次只能選擇 一個左側欄位的 checkbox

------------------------------------------------------
- #### I. 將 .ui 檔 轉成 .py檔 的轉檔指令 pyuic5 -x weather.ui -o storeui.py [weather.ui 為自己設定在 Qt 的 檔名、storeui.py 為自己命名存放轉檔後的位置名稱]

- #### II. *打包 exe 前*，將所有資料 [含.py、.ui 、所有圖片檔] 要放在同一層資料裡面、確認指令有下在該層級的資料夾

- #### III. *打包 exe 指令* : pyinstaller -F AJ__one.py --noconsole (-F 雜檔包一起、[AJ__one 為自己的 py檔名]、--noconsole 讓背景黑色的 cmd 執行視窗 不要跳出 [在spec檔 裡也可以把 console 改 False])

- #### IV. *打包後*，只需要看 *dist 裡面的 那個資料夾* 就好

- #### V. 透過 _import base64_，設計把 *png、jpg、gif* 檔，包進py檔裡面，但目前只能在本機端執行


