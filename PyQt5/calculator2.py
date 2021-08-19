from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_add.clicked.connect(self.calculate)
        self.ui.btn_subs.clicked.connect(self.calculate)
        self.ui.btn_multi.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender()
        
        if(sender.text() == "Addition"):
            result = int(self.ui.txt_number1.text()) + int(self.ui.txt_number2.text())
            self.ui.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Substraction"):
            result = int(self.ui.txt_number1.text()) - int(self.ui.txt_number2.text())
            self.ui.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Multiplication"):
            result = int(self.ui.txt_number1.text()) * int(self.ui.txt_number2.text())
            self.ui.lbl_result.setText("RESULT : " + str(result))
        elif(sender.text() == "Division"):
            try:
                result = int(self.ui.txt_number1.text()) / int(self.ui.txt_number2.text())
            except Exception as exc:
                self.ui.lbl_result.setText("RESULT : " + str(exc))
            else:
                self.ui.lbl_result.setText("RESULT : " + str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()