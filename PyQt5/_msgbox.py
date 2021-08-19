from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from _msgboxForm import Ui_MainWindow
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.showDialog)

    def showDialog(self):
        result = QMessageBox.question(self,"Close Application","Are you sure ?",
                                      QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("Clicked ok")
            QtWidgets.qApp.quit()
        else:
            print("No click.")
                

        # msg = QMessageBox()

        # msg.setWindowTitle("Close Application")
        # msg.setWindowIcon(QIcon("baticon.png"))
        # msg.setText("Are you sure ?")
        # msg.setIcon(QMessageBox.Question)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Cancel)
        # msg.setDetailedText("details...")
        # msg.buttonClicked.connect(self.popup_button)

        # x = msg.exec_()
        # print(x)
    
    # def popup_button(self,i):
    #     print(i.text())

    #     if i.text() == 'OK':
    #         print("Pressed OK")
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Ignore':
    #         print("Pressed Ignore")
    #     elif i.text() == 'Cancel':
    #         print("Pressed CANCEL")
        


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())