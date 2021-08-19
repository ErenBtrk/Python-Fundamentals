from PyQt5 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rbt_turkey.setChecked(True)
        self.ui.rbt_pschool.setChecked(True)

        self.ui.rbt_turkey.toggled.connect(self.onClickedCountry)
        self.ui.rbt_azerbaijan.toggled.connect(self.onClickedCountry)
        self.ui.rbt_germany.toggled.connect(self.onClickedCountry)
        self.ui.rbt_greece.toggled.connect(self.onClickedCountry)

        self.ui.rbt_bachelor.toggled.connect(self.onClickedEducation)
        self.ui.rbt_masters.toggled.connect(self.onClickedEducation)
        self.ui.rbt_hschool.toggled.connect(self.onClickedEducation)
        self.ui.rbt_pschool.toggled.connect(self.onClickedEducation)

        self.ui.bt_country.clicked.connect(self.getSelectedCountry)
        self.ui.bt_education.clicked.connect(self.getSelectedEducation)

    def onClickedCountry(self):
        rb = self.sender()
        if(rb.isChecked()):
            print("Picked country : " + rb.text())

    def onClickedEducation(self):
        rb = self.sender()
        if(rb.isChecked()):
            print("Picked education level : " + rb.text())

    def getSelectedCountry(self):
        items = self.ui.groupBox_Countries.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if(rb.isChecked()):
                self.ui.lbl_country.setText("Selected Country : " + rb.text())

    def getSelectedEducation(self):
        items = self.ui.groupBox_education.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if(rb.isChecked()):
                self.ui.lbl_education.setText("Selected Education : " + rb.text())


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())