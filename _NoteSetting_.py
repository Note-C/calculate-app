from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json

with open("style.json") as file:
    Data=file.read()#to read values into the 'style.json' 
DataStyle=json.loads(Data)
Note_font=DataStyle["NoteFont"]

num1=5
num2=100
#to make Note selection 
class _Note_layer(QWidget):
    def __init__(self,main):
        super().__init__()
        self.main=main
        self.midterm_Note=QComboBox(self.main)
        self.finaly_Note=QComboBox(self.main)
        self.HWork_note=QComboBox(self.main)
        self.Project_note=QComboBox(self.main)
       
        
        #create value list  
        self.NoteList()
        self.noteStyle()
    def NoteList(self):
        for valueNote in range(10,num2+num1,num1):
            self.midterm_Note.addItem(str(valueNote))
            self.finaly_Note.addItem(str(valueNote))
            self.HWork_note.addItem(str(valueNote))
            self.Project_note.addItem(str(valueNote))
        
        self.finaly_Note.move(640,210)
        self.midterm_Note.move(640,150)
        self.HWork_note.move(640,290)
        self.Project_note.move(640,350)
    def noteStyle(self):
        self.midterm_Note.setStyleSheet(Note_font)
        self.finaly_Note.setStyleSheet(Note_font)
        self.HWork_note.setStyleSheet(Note_font)
        self.Project_note.setStyleSheet(Note_font)