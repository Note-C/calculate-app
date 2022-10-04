#from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qtwidgets import *
import json
import sys



with open("style.json") as file:
    Data=file.read()#to read values into the 'style.json' 
DataStyle=json.loads(Data)

#text 
file_location=sys.path[0]+"\\plainText\\about.txt"
with open(file_location) as file:
    md=file.read()
textMd=str(md)

ButtonFont=DataStyle["Button"]
ButtonTextFont=DataStyle["Button-text"]
CheckFont=DataStyle["QcheckBox"]
aboutFont=DataStyle["about"]
aboutText=DataStyle["about-text"]
Img=sys.path[0]+"\\log\\04.jpg"

#to make logo Bar
class _LogoBar_(QWidget):
    def __init__(self,main):
        super().__init__()
        self.main=main
        #BackGround logo
        self.setFixedSize(500,500)
        
        self.label=QLabel(self.main)
        self.text=QLabel(textMd,self.main)
        #social network
        self.Social()
        self.label.setStyleSheet(aboutFont)
        self.text.setStyleSheet(aboutText)
        self.logImg=QPixmap(Img)
        #size=self.logImg.scaled(250,250)
        self.label.setPixmap(self.logImg)
        
        self.label.resize(self.logImg.width(),self.logImg.height())
        self.label.move(0,0)
        self.label.setFixedHeight(650)
        self.label.setFixedWidth(300)
        self.text.move(30,140)
        self.text.setFixedHeight(200)
        self.text.setFixedWidth(250)
    def Social(self):
        insta=QLabel('<a href="https://www.instagram.com/notecofficial/">Instagram</a>',self.main)
        twit=QLabel('<a href="https://twitter.com/NotecOfficial">Twitter</a>',self.main)
        Like=QLabel('<a href="#">Linkedin</a>',self.main)
        insta.setStyleSheet(self.like_style())
        twit.setStyleSheet(self.like_style())
        Like.setStyleSheet(self.like_style())
        insta.move(40,440)
        twit.move(40,480)
        Like.move(40,520)

    def like_style(self):
        style="""
            QLabel {
                background-color:white;
                font-size:15px;
                font-family: 'Trebuchet MS', sans-serif;
                padding:5px 10px;
                
            }
            :hover{
                border:1px solid #FBCB0A;
                border-radius:5%;
            }
        """
        return style
        


class _MainButtons_(QWidget):
    def __init__(self,main):
        super().__init__()
        self.main=main
       
        _LogoBar_(self.main)
        #text Buttons
        self.midterm=QLineEdit(self.main)
        self.finaly=QLineEdit(self.main)
        # to crearte homework and project
        self.project=QLineEdit(self.main)
        self.hwork=QLineEdit(self.main)
        self.pro_button(self.project)
        self.HW_button(self.hwork)
        
        self.mid_button()
        self.fin_button()
       
    def mid_button(self):
        self.midterm.setFixedWidth(100)
        self.midterm.setFixedHeight(40)
        self.midterm.setStyleSheet(ButtonFont)
        self.midterm.move(460,150)
        self.midterm.setMaxLength(3)
        self.midterm.setPlaceholderText("Giriş")
        self.midterm.setValidator(QIntValidator())
        self.text_button("Viza Puanı",360,150)
        
    def fin_button(self):
        self.finaly.setFixedWidth(100)
        self.finaly.setFixedHeight(40)
        self.finaly.setStyleSheet(ButtonFont)
        self.finaly.move(460,210)
        self.finaly.setMaxLength(3)
        self.finaly.setPlaceholderText("Giriş")
        self.finaly.setValidator(QIntValidator())
        self.text_button("Final Puanı",360,210)
        
    def HW_button(self,Hwork):
        Hwork.setFixedWidth(100)
        Hwork.setFixedHeight(40)
        Hwork.setStyleSheet(ButtonFont)
        Hwork.move(460,290)
        Hwork.setMaxLength(3)
        Hwork.setPlaceholderText("Giriş")
        Hwork.setValidator(QIntValidator())
        self.text_button("Ödev Puanı",360,290)

    def pro_button(self,project):
        project.setFixedWidth(100)
        project.setFixedHeight(40)
        project.setStyleSheet(ButtonFont)
        project.move(460,350) 
        project.setMaxLength(3)
        project.setPlaceholderText("Giriş")
        project.setValidator(QIntValidator())
        self.text_button("Sunum Puanı",350,350)
    def text_button(self,text,x,y):
        self.txt=QLabel(text,self.main)
        self.txt.move(x,y)
        self.txt.setStyleSheet(ButtonTextFont)
