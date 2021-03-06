from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  
class Window(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Python ") 
        self.setGeometry(100, 100, 600, 400)
        self.update
        self.UiComponents() 
        self.show() 
        
    # method for widgets 
    def UiComponents(self): 
        # creating a push button 
        self.button = QPushButton("Start", self) 
  
        self.button.setGeometry(200, 150, 100, 100) 
        self.button.setCheckable(True)

        self.button.clicked.connect(self.clickme)
        self.button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50;  border : 2px solid black;"
                             "background-color : red;"
                             "}"
                             )    
  
    def clickme(self):
        if self.button.isChecked():
            self.button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50;  border : 2px solid black;"
                             "background-color : green;"
                             "}"
                             ) 
        else:
            self.button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50;  border : 2px solid black;"
                             "background-color : red;"
                             "}"
                             ) 
        


App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 