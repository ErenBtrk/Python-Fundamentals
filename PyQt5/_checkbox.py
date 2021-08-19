import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_cinema.stateChanged.connect(self.show_state)
        self.ui.cb_reading.stateChanged.connect(self.show_state)
        self.ui.cb_sports.stateChanged.connect(self.show_state)

        self.ui.btn_save_hobbies.clicked.connect(self.getAllHobbies)
        self.ui.btn_save_lectures.clicked.connect(self.getAllLectures)
    
    def show_state(self,value):
        cb = self.sender()

        print(value)
        print(cb.text())
        print(cb.isChecked())

    def getAllHobbies(self):
        result = ""
        items = self.ui.groupHobbies.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if(cb.isChecked()):
                result += cb.text() + '\n'

        self.ui.lbl_result_hobbies.setText(result)

    def getAllLectures(self):
        result = ""
        items = self.ui.groupLectures.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if(cb.isChecked()):
                result += cb.text() + '\n'

        self.ui.lbl_result_lectures.setText(result)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
