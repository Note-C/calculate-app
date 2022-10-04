from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import json
from _mainCalculate import CalculateAndCancel

#logo
Img=[sys.path[0]+"\\log\\log.jpg",sys.path[0]+"\\log\\backLog.png"]


with open("style.json") as file:
    Data=file.read()#to read values into the 'style.json' 
DataStyle=json.loads(Data)
#widnow gemoetry
ScreenX=DataStyle["Screen-Size"]["Width"]
ScreenY=DataStyle["Screen-Size"]["Height"]

def ColorTheme():
    global DataStyle
    getTheme=DataStyle["Color-Theme"]
    return str(getTheme) 

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(ColorTheme())
        self.setFixedSize(ScreenX,ScreenY)#that is method to set the fixed size of the window.
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(Img[0]))
        self.setWindowTitle("notec")
        self.title_bar_Layout=QVBoxLayout()
        self.title_bar_Layout.setContentsMargins(10,10,10,10)
       
        self.setLayout(self.title_bar_Layout)
        CalculateAndCancel(self)
        
        
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    Core=App()
    Core.show()
    app.exec_()