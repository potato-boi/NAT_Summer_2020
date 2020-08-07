from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  
class Window(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Python ") 
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents() 
        self.show() 
        
    # method for widgets 
    def UiComponents(self): 
        # creating a push button 
        button = QPushButton("Start", self) 
  
        button.setGeometry(200, 150, 100, 100) 

        button.clicked.connect(self.clickme)
        button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50;  border : 2px solid black;"
                             "background-color : red;"
                             ""
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )    
  
    def clickme(self): 
        import send
        print('pressed')

App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 