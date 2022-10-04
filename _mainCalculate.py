from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from click import style
from _NoteSetting_ import _Note_layer
from _ButtonSetting_ import _MainButtons_
import sys


def ButtonFont():
    style=""" 
            QPushButton {
                background-color:#590696;
                font-weight:bold;
                font-size:15px;
                font-family: 'Trebuchet MS', sans-serif;
                border:1px solid #FBCB0A;
                border-radius:15%;
                text-transform: uppercase;
                color:white;
            }
            QPushButton:hover {
                background-color:#FBCB0A;
                color:balck;
                
            }
    """
    return style
class CalculateAndCancel(QWidget):
    def __init__(self,main):
        super().__init__()
        self.main=main
        self.getNote=_Note_layer(self.main)
        self.getMButtons=_MainButtons_(self.main)
        #to make Buttons 
        self.Entiry=QPushButton("Calculate",self.main)
        self.Cancel=QPushButton("Cancel",self.main)
        self.Cancel.clicked.connect(sys.exit)
        self.Entiry.clicked.connect(lambda:self.Process())
        #Display value
        self.show=Display(self.main)
        
        self.StyleButtons()
    def StyleButtons(self):
        self.Entiry.move(640,420)
        self.Cancel.move(450,420)
        self.Entiry.setFixedSize(120,45)
        self.Cancel.setFixedSize(120,45)
        self.Entiry.setStyleSheet(ButtonFont())
        self.Cancel.setStyleSheet(ButtonFont())
        self.Entiry.setToolTip("this is show calculate.")
        self.Cancel.setToolTip("this is for compile exit of App")
    @classmethod
    def noteFormula(cls,x,y,a,z):
        priceA=100
        priceB=[a,z]
        return ((x*priceB[0])/priceA)+((y*priceB[1])/priceA)
    @classmethod
    def Formula_other_(cls,x,y,z):
        priceB=z
        return x+((y*priceB)/100)
   
    def Process(self):
        #part 1: to get note value
        self.midterm_id=self.getMButtons.midterm.text()
        self.finaly_id=self.getMButtons.finaly.text()
        self.hwork_id=self.getMButtons.hwork.text()
        self.project_id=self.getMButtons.project.text()
        #part 2: to get note price value
        self.mid_note_id=int(self.getNote.midterm_Note.currentText())
        self.fin_note_id=int(self.getNote.finaly_Note.currentText())
        self.hwork_note_id=int(self.getNote.HWork_note.currentText())
        self.project_note_id=int(self.getNote.Project_note.currentText())
        #to get formula
        
        try:
            if((int(self.midterm_id)<=100 and int(self.finaly_id)<=100)and(int(self.hwork_id)<=100 and int(self.project_id)<=100)):
                text=self.noteFormula(int(self.midterm_id),int(self.finaly_id),self.mid_note_id,self.fin_note_id)+self.noteFormula(int(self.hwork_id),int(self.project_id),
                self.hwork_note_id,self.project_note_id)
                self.show.text.setText("Genel Başarı: "+str(text))
        except ValueError:
            try:
                formula_set=self.noteFormula(int(self.midterm_id),int(self.finaly_id),self.mid_note_id,self.fin_note_id)
                if(self.hwork_id=="" and self.project_id==""):
                    text=self.noteFormula(int(self.midterm_id),int(self.finaly_id),self.mid_note_id,self.fin_note_id)
                    self.show.text.setText("Genel Başarı: "+str(text))
                elif(self.hwork_id==""):
                    text=self.Formula_other_(formula_set,int(self.project_id),self.project_note_id)
                    self.show.text.setText("Genel Başarı: "+str(text))
                elif(self.project_id==""):
                    text=self.Formula_other_(formula_set,int(self.hwork_id),self.hwork_note_id)
                    self.show.text.setText("Genel Başarı: "+str(text))
            except:
                
                self.show.text.setText("Değerler Boş")

class Display(QWidget):
    def __init__(self,main):
        self.text=QLabel("Sınav Puanızı hesaplayın...",main)
        self.TextStyle()
    def TextStyle(self):
        self.text.move(450,480)
        self.text.setFixedHeight(120)
        self.text.setFixedWidth(310)
        self.text.setStyleSheet(self.StyleFont())

    def StyleFont(self):
        style="""
            
            border:1px solid white;border-radius: 10%;
            font-size:20px;
            font-weight:bold; 
            font-family: 'Trebuchet MS', sans-serif; 
            background-color:#fafafa;
            padding:0px 5px 65px;
        
        """
        return style
