import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("baticon.png"))
        self.setToolTip("My Tooltip")
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Your Name : ")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Your Surname : ")
        self.lbl_surname.move(50,60)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,60)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("SAVE")
        self.btn_save.move(150,110)
    
        self.btn_save.clicked.connect(self.clickedFunc)

    def clickedFunc(self):
        self.lbl_result.setText("Name : " + self.txt_name.text() + " Surname : " + self.txt_surname.text())
        with open("names.txt","a") as file:
            file.write(self.txt_name.text()+ ' ' +self.txt_surname.text() + '\n')
            print("Saved.")
            self.txt_name.setText("")
            self.txt_surname.setText("")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()



    




