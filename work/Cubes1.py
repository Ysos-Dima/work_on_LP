import random
import sys
from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QApplication,QListWidget , QMainWindow , QLabel,  QVBoxLayout, QGridLayout, QWidget, QLineEdit, QPushButton, QMessageBox

class Window(QMainWindow):
        def __init__(self):    
            super().__init__()
            self.setFixedSize(QSize(400,300))
             
            self.setWindowTitle("Вероятность выпадения чисел")
            
            but1=QPushButton(self)
            but1.setText("Рассчитать вероятность для всех чисел")
            but1.setFixedSize(222,25)
            but1.move(0,0)
            but1.setCheckable(True)
            
            but1.clicked.connect(self.the_button_was_toggled)
            
            info1=QLineEdit(self)
            info1.setText("Колличество кубиков")
            info1.setFixedSize(130,25)
            info1.move(92,23)
            info1.setDisabled(True)

            self.vvod1=QLineEdit(self)
            self.vvod1.setText("2")
            self.vvod1.move(0,23)
            self.vvod1.setFixedSize(92,25)

            info2=QPushButton(self)
            info2.setText("Колличество бросков")
            info2.setFixedSize(130,25)
            info2.move(92,46)
            info2.setDisabled(True)
            
            self.vvod2=QLineEdit(self)
            self.vvod2.setText("1")
            self.vvod2.move(0,46)
            self.vvod2.setFixedSize(92,25)
            
            self.rez = QListWidget(self)
            self.rez.addItems(["Результат:"])
            self.rez.move(0,70)
            self.rez.setFixedSize(222,200)

            but3=QPushButton(self)
            but3.setText("Рассчитать для одного числа")
            but3.setFixedSize(180,25)
            but3.move(221,0)
            but3.setCheckable(True)
            
            but3.clicked.connect(self.button3)

            self.vvod3=QLineEdit(self)
            self.vvod3.setText("3")
            self.vvod3.move(221,24)
            self.vvod3.setFixedSize(30,23)

            self.rez2 = QListWidget(self)
            self.rez2.addItems(["Результат:"])
            self.rez2.move(251,24)
            self.rez2.setFixedSize(149,60)

        
        def the_button_was_toggled(self):
            
            self.rez.clear()  
            self.rez.addItems(["Результат:"])
            cube=int(self.vvod1.text())
            throw=int(self.vvod2.text())
            
            
            self.chisla=[]
            for n in range(throw):
                sm=0
                for h in range(cube):
                    x=random.randint(1,6)
                    sm+=x
                self.chisla.append(sm)
            ch=1
            for x in range(6*(cube)):
                    
                a=self.chisla.count(ch)

                rezult=str(ch)+"="+str(float(a/len(self.chisla)*100))+"%"
                      
                self.rez.addItem(str(rezult))

                ch+=1
        def button3(self):
            ch=int(self.vvod3.text())
            self.rez2.clear()
            self.rez2.addItems(["Результат:"])
            
            

                    
            a=self.chisla.count(ch)

            proc=str(ch)+"="+str(float(a/len(self.chisla)*100))+"%"
                      
            self.rez2.addItem(str(proc))
            
        
                
                    

            

            
        
app = QApplication(sys.argv)

window=Window()
window.show()

app.exec()