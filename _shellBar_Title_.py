#the app .. 
import sys

from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json



title="#251D3A"
#we have been production this json file ,so that file is a style app.
with open("style.json") as file:
    Data=file.read()#to read values into the 'style.json' 
DataStyle=json.loads(Data)#before to don't get all values on the 'style.json'
#widnow gemoetry
ScreenX=DataStyle["Screen-Size"]["Width"]
ScreenY=DataStyle["Screen-Size"]["Height"]
#to set Logo
getLogoFont=DataStyle["Logo"]["Font"]
# title log and a lot of image or logo
Img=[sys.path[0]+"\\log\\log.jpg",sys.path[0]+"\\log\\backLog.png"]

def buttonClose():
    global DataStyle
    getButton1=DataStyle["title-bar-button"][0]
    button1Bar=getButton1["button1"]
    return button1Bar
def buttonOff():
    global DataStyle
    getButton2=DataStyle["title-bar-button"][1]
    button2Bar=getButton2["button2"]
    return str(button2Bar)
def buttonEmpty():
    global DataStyle
    getButton3=DataStyle["title-bar-button"][2]
    button3Bar=getButton3["button3"]
    return str(button3Bar)
def ColorTheme():
    global DataStyle
    getTheme=DataStyle["Color-Theme"]
    return str(getTheme)

#and to make sepecific the "Title Bar" 
#we have to use other class because these codes can be seeing confused.

class _TitleBar_H(QWidget):
    def __init__(self,main):
        super().__init__()
        self.main=main
        self.layoutH=QHBoxLayout()
        self.TitleLog()
        self.title=QLabel("App - NoteC")
        self.title.setStyleSheet(getLogoFont)
        self.layoutH.addWidget(self.title)
        
        self.layoutH.setContentsMargins(0,0,0,0)
        
        self.button2()
        self.button3()
        self.button1()
        self.title.setFixedHeight(35)
        #self.title.setFixedHeight(self.main.width())
        self.setLayout(self.layoutH)
       

    def button1(self):
        self.btn_close=QPushButton(self.main)
        self.btn_close.setFixedSize(20,20)
        self.btn_close.setStyleSheet(buttonClose())
        self.btn_close.clicked.connect(self.buttonClose)
        self.layoutH.addWidget(self.btn_close)
    def button2(self):
        self.btn_off=QPushButton(self.main)
        self.btn_off.setStyleSheet(buttonOff())
        self.btn_off.setFixedSize(20,20)
        self.btn_off.clicked.connect(self.buttonOff)
        self.layoutH.addWidget(self.btn_off)
    def button3(self):
        self.btn_empty=QPushButton(self.main)
        self.btn_empty.setStyleSheet(buttonEmpty())
        self.btn_empty.setFixedSize(20,20)
        self.layoutH.addWidget(self.btn_empty)

    def TitleLog(self):
        """self.log=QLabel()
        self.img=QPixmap(Img[0])
        #size=self.img.scaled(60,60)
        self.log.setPixmap(self.img)
        self.layoutH.addWidget(self.log)
        """
    
    def buttonClose(self):
        self.main.close()
    def buttonOff(self):
        self.main.showMinimized()

    def mousePressEvent(self, e):
        self.oldPosition = e.globalPos()
    def mouseMoveEvent(self, e):
        self.delta= QPoint(e.globalPos() - self.oldPosition)
        self.main.move(self.main.x() + self.delta.x(), self.main.y() + self.delta.y())
        self.oldPosition = e.globalPos()