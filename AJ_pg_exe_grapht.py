from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from bs4 import BeautifulSoup as bs
from storeui import Ui_Form
import os, sys, base64, requests

# 網路教學方式: 讀取圖片檔，在寫入圖片檔 (用二進制方式、base64模組)
jpg_path = 'C:\\Users\\jac13\\OneDrive\\桌面\\天氣報告\\bg_stripes.jpg'
png_path = 'C:\\Users\\jac13\\OneDrive\\桌面\\天氣報告\\tw.png'
gif_path = 'C:\\Users\\jac13\\OneDrive\\桌面\\天氣報告\\spongebob.gif'

# 打包 jpg 進 py檔
with open(jpg_path, 'rb') as j:
    image_data = j.read()
    base64_data = base64.b64encode(image_data)  # base64编码
    print(base64_data)
    print(type(base64_data))

with open('bg_stripes.jpg', 'wb') as j:
    jiema = base64.b64decode(base64_data)  # 解码
    j.write(jiema)  # 将解码得到的数据写入到图片中
    #print(jiema)

# 打包 png 進 py檔
with open(png_path, 'rb') as p:
    image_data2 = p.read()
    base64_data2 = base64.b64encode(image_data2)  # base64编码
    print(base64_data2)
    print(type(base64_data2))

with open('tw.png', 'wb') as p:
    jiema2 = base64.b64decode(base64_data2)  # 解码
    p.write(jiema2)  # 将解码得到的数据写入到图片中

# 打包 gif 進 py檔
with open(gif_path, 'rb') as g:
    image_data3 = g.read()
    base64_data3 = base64.b64encode(image_data3)  # base64编码
    print(base64_data3)
    print(type(base64_data3))

with open('spongebob.gif', 'wb') as g:
    jiema3 = base64.b64decode(base64_data3)  # 解码
    g.write(jiema3)  # 将解码得到的数据写入到图片中

# 網路教學方式-2:
'''with open("C:\\Users\\jac13\\OneDrive\\桌面\\weath\\tw.png","rb") as f:
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())
    print(base64_data)#输出生成的base64码

#img_str = 'abcdefgh12345oK='#比如生成后的码就这么放，替换下面的base64_data即可
img_data = base64.b64decode(base64_data)
# 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。
with open('tw.jpg', 'wb') as f:
    f.write(img_data)'''

# 自學聖經-書本 教學方式
'''#加入自訂的 base_path()函式
import os, sys, glob
def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path) 

source_dir=base_path('combin/')
#a = glob.glob(source_dir+"*.jpg")
b = glob.glob(source_dir+"*.png")
#c = glob.glob(source_dir+"*.gif")'''

# 自學聖經-書本 [33.5 章節]-教學方式
'''def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path) 
    
#tmp=base_path("") #取得暫存目錄
cwd=os.getcwd()   #取得目前的工作目錄

file1="bg.jpg"
#file2=os.path.join(tmp,"file2.txt")
file3=os.path.join(cwd,"tw.png")

f1=open(file1,'rb')  #寫入工作目錄
#f1.write()
f1.close()
print(file1,"寫入成功!")

f2=open(file2,'w')  #寫入 tmp 目錄
f2.write("file2 txt")
f2.close()
print(file2,"寫入成功!")

f3=open(file3,'rb') #寫入 pwd 目錄
#f3.write()
f3.close()
print(file3,"寫入成功!")'''

try:
    def loc_taipei():
        global loc
        loc="6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa"
    def loc_newtaipei():
        global loc
        loc="5f5c20be14aba17192a3bb3a57511db1ebf2cbdd439af51cd03fa623d67e2de1"
    def loc_keelung():
        global loc
        loc="2d7ad0763322f8f204948bab69b8437cc74e2cb1fddc0b11261dc6666360749e"
    def loc_taoyuan():
        global loc
        loc="efbf308224729b20c95ff9150f731657639bc63cce74c8c098357587b7bbc9c4"
    def loc_hsinchucity():
        global loc
        loc="9d98eb3f97a83330c0599a7548c3c7b47163615858673cfee2406e208ce20604"
    def loc_hsinchucountry():
        global loc
        loc="57a7b26fe9f26d76db41f36fb9bc87e0deca14bde2053885dad839edf0e26fc3"
    def loc_miaoli():
        global loc
        loc="b994c89cc0ff3b6b56814e2730a58c821d2585ce6d3f190ea6a8c502c82268c2"
    def loc_taichung():
        global loc
        loc="8e095973cc14ab3966eab1a0c6a1b04f5291e61049bff4cb42a510b3881afec9"
    def loc_changhua():
        global loc
        loc="50f0afa948f93e0309ee2f37a6d34beaf66a79e423e4dec6b9bc063ce8d993c8"
    def loc_yunlin():
        global loc
        loc="ea62fd1222f79ea36b16907f723f715e9e5640c8f1dbe52360334dde168f3410"
    def loc_nantou():
        global loc
        loc="d8b83853a6cc59e5bb3fe1e512cc4be8a3e5c1842889f42c5272bc1b14c2abb9"
    def loc_chaiyicity():
        global loc
        loc="083ec430bd75b8e34579f93ce7c6c033e47d58eca20302a4ede6e3914cd1150a"
    def loc_chaiyicountry():
        global loc
        loc="715bc33c482ab5cf9fa7ee48fefbf5547d8ac5da7025db275d5b43d4d000785a"
    def loc_tainan():
        global loc
        loc="cb9a4442e9bf7da0ece89bd21a5161210e79cccc0ec2647b3565977e7a278c31"          
    def loc_kaohsiung():
        global loc
        loc="48697cc4c9743031df643ebe553fc08fd83bf2e96d7c7f58c0db435d5888131f"
    def loc_pingtung():
        global loc
        loc="2303e8481a2d2f9b32e5343dc3661a921123f3ccdd277563e4b6d7771d53a244"
    def loc_taitung():
        global loc
        loc="081fa0de6091622e509eef3a5b3346083026cfb067ee1df44c55c15919096639"
    def loc_hualien():
        global loc
        loc="6e37fc12427c24cb9ae8e50a596754434e8244b28c1a3d25b8122fb3a0dca2f6"
    def loc_yilan():
        global loc
        loc="509a0202845cfc5a9b7e8c39e61323b593893292803d99c5fa3fe0f572f2ddff"
    def loc_lianjing():
        global loc
        loc="1fec843e21c6886161e8680edfcc424b2bd7c0a2c7cbe8996fa5473d580c8e7c"
    def loc_kinmen():
        global loc
        loc="e0c8bf85249767181baf1c831c322a7b5a7e8df91ea86434ad6b1a1ba47f6ef8"
    def loc_penghu():
        global loc
        loc="952e360e0b0a5052fd0f5bd4fd190b928c930897dd3860dc5f5628af71e79ea5"
    def pic_click(event):                           #點擊背景的動作
        message=QMessageBox()
        message.setWindowTitle('show')
        message.setInformativeText('請先選擇要顯示的資訊，並點選地區')
        message.exec_()
    def GIF_WAIT():
        message=QMessageBox()
        message.setWindowTitle('WAIT')
        dialog = QDialog()
        dialog.setWindowTitle('')        
        layout = QVBoxLayout(dialog)
        label = QLabel(dialog)
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        label.setScaledContents(True)
        movie = QMovie("spongebob.gif")
        label.setMovie(movie)
        movie.start()
        layout.addWidget(label)
        message.layout().addWidget(dialog)
        message.exec_() 
        
    def action():
        GIF_WAIT()
        res = requests.get("https://weather.com/zh-TW/weather/today/l/"+loc)
        soup = bs(res.text)
        time = soup.find_all("div",class_="CurrentConditions--header--kbXKR")                                          #縣市地點
        temp = soup.find_all("div",class_="Column--temp--1sO_J")                                                           #溫度
        wind = soup.find_all("span",class_="Wind--windWrapper--3Ly7c undefined")                                           #風速
        aqi = soup.find_all("div",class_="AirQuality--col--3I-4C")                                                         #空氣指標
        rain = soup.find_all("span",class_="Column--precip--3JCDO")                                                        #降雨機率
        sit = soup.find_all("div",class_="CurrentConditions--phraseValue--mZC_p")                                          #天氣概況
        basic=str(time[0].h1.text.split(",")[1][1:])
        show_time='當前時間:'+str(time[0].span.text.split(" ")[1])
        ans=''
        if ui.temp.isChecked():
            ans=basic,'\n',show_time,'\n',str("溫度 "+temp[0].span.text+"C")
        elif ui.rain.isChecked():
            ans=basic,'\n',show_time,'\n',str(rain[2].text)
        elif ui.humi.isChecked():
            ans=basic,'\n',show_time,'\n',str("空氣品質指標 "+aqi[0].text)
        elif ui.wing.isChecked():
            ans=basic,'\n',show_time,'\n',str(wind[0].text)
        elif ui.overview.isChecked():
            ans=basic,'\n',show_time,'\n',str(sit[0].text)
        else:
            message=QMessageBox()
            message.setWindowTitle(" error ")
            message.setInformativeText("請選擇要顯示的資訊")
            message.exec_() 
        ui.label.setText('\n'.join(ans))
        
    def button_connet():
        ui.label_3.mouseReleaseEvent=pic_click
        ui.chaiyicity.clicked.connect(loc_chaiyicity)
        ui.chaiyicity.clicked.connect(action)
        ui.chaiyicountry.clicked.connect(loc_chaiyicountry)
        ui.chaiyicountry.clicked.connect(action)
        ui.changhua.clicked.connect(loc_changhua)
        ui.changhua.clicked.connect(action)
        ui.hsinchucity.clicked.connect(loc_hsinchucity)
        ui.hsinchucity.clicked.connect(action)
        ui.hsinchucountry.clicked.connect(loc_hsinchucountry)
        ui.hsinchucountry.clicked.connect(action)
        ui.hualien.clicked.connect(loc_hualien)
        ui.hualien.clicked.connect(action)
        ui.kaohsiung.clicked.connect(loc_kaohsiung)
        ui.kaohsiung.clicked.connect(action)
        ui.Keelung.clicked.connect(loc_keelung)
        ui.Keelung.clicked.connect(action)
        ui.kinmen.clicked.connect(loc_kinmen)
        ui.kinmen.clicked.connect(action)
        ui.lianjing.clicked.connect(loc_lianjing)
        ui.lianjing.clicked.connect(action)
        ui.miaoli.clicked.connect(loc_miaoli)
        ui.miaoli.clicked.connect(action)
        ui.nantou.clicked.connect(loc_nantou)
        ui.nantou.clicked.connect(action)
        ui.newtaipei.clicked.connect(loc_newtaipei)
        ui.newtaipei.clicked.connect(action)
        ui.penghu.clicked.connect(loc_penghu)
        ui.penghu.clicked.connect(action)
        ui.taichung.clicked.connect(loc_taichung)
        ui.taichung.clicked.connect(action)
        ui.pingtung.clicked.connect(loc_pingtung)
        ui.pingtung.clicked.connect(action)
        ui.tainan.clicked.connect(loc_tainan)
        ui.tainan.clicked.connect(action)
        ui.Taipei.clicked.connect(loc_taipei)
        ui.Taipei.clicked.connect(action)
        ui.taitung.clicked.connect(loc_taitung)
        ui.taitung.clicked.connect(action)
        ui.Taoyuan.clicked.connect(loc_taoyuan)
        ui.Taoyuan.clicked.connect(action)
        ui.yilan.clicked.connect(loc_yilan)
        ui.yilan.clicked.connect(action)
        ui.yunlin.clicked.connect(loc_yunlin)
        ui.yunlin.clicked.connect(action)
        group=QButtonGroup(Form)
        group.addButton(ui.temp)
        group.addButton(ui.rain)
        group.addButton(ui.wing)
        group.addButton(ui.humi)
        group.addButton(ui.overview)

except:
    message=QMessageBox()
    message.setWindowTitle(" error ")
    message.setInformativeText("請先選擇要顯示的資訊，並點選地區")
    message.exec_()     

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
button_connet()
Form.show()
sys.exit(app.exec_())


