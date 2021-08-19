import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QFont

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number 1 : ")
        self.lbl_number1.move(50,30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(200,32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number 2 : ")
        self.lbl_number2.move(50,80)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,300)
        self.lbl_result.setFont(QFont('Times', 10))

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(200,32)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Addition")
        self.btn_add.move(150,130)
        self.btn_add.clicked.connect(lambda : self.calculate())

        self.btn_multip = QtWidgets.QPushButton(self)
        self.btn_multip.setText("Multiplication")
        self.btn_multip.move(150,170)
        self.btn_multip.clicked.connect(lambda : self.calculate())

        self.btn_subs = QtWidgets.QPushButton(self)
        self.btn_subs.setText("Substraction")
        self.btn_subs.move(150,210)
        self.btn_subs.clicked.connect(lambda : self.calculate())

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Division")
        self.btn_div.move(150,250)
        self.btn_div.clicked.connect(lambda : self.calculate())

    def calculate(self):
        sender = self.sender()
        
        if(sender.text() == "Addition"):
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
            self.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Substraction"):
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
            self.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Multiplication"):
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
            self.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Division"):
            try:
                result = int(self.txt_number1.text()) / int(self.txt_number2.text())
            except Exception as exc:
                self.lbl_result.setText("RESULT : " + str(exc))
            else:
                self.lbl_result.setText("RESULT : " + str(result))
                
            
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()