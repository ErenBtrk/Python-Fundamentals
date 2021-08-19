import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Application")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon("baticon.png"))
    win.setToolTip("My Tooltip")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Your Name : ")
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Your Surname : ")
    lbl_surname.move(50,60)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,60)

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("SAVE")
    btn_save.move(150,110)
    
    btn_save.clicked.connect(lambda: clicked(txt_name,txt_surname))

    win.show()
    sys.exit(app.exec_())

def clicked(txt_name,txt_surname):
    with open("names.txt","a") as file:
        file.write(txt_name.text()+ ' ' +txt_surname.text())
        print("Saved.")
        txt_name.setText("")
        txt_surname.setText("")
 



    

window()



#QLabel
#QComboBox
#QCheckBox
#QRadioButton
#QPushButton
#QTableWidget
#QLineEdit
#QSlider
#QProgressBar