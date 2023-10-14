from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from password import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app =  QApplication([])
window = Widget()

def generation():
    digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['g', 'l', 'm']


btn_OK.clicked.connect(generation)

window.show()
app.exec_()
