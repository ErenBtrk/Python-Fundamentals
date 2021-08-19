from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.cb_cities.addItem("Ankara")
        # self.ui.cb_cities.addItem("Istanbul")
        # self.ui.cb_cities.addItem("Izmir")
        # self.ui.cb_cities.addItem("Sivas")
        # self.ui.cb_cities.addItem("Corum")
        # self.ui.cb_cities.addItems(["Trabzon","Adana","Rize"])

        self.ui.btn_loadItems.clicked.connect(self.loadItems)
        self.ui.btn_getItem.clicked.connect(self.getItem)
        self.ui.btn_clearItems.clicked.connect(self.clearItems)

        self.ui.cb_cities.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cb_cities.currentIndexChanged[str].connect(self.selectedChangedText)

    def loadItems(self):
        cities = ["Ankara","Istanbul","Izmir","Corum","Trabzon","Adana","Rize"]

        self.ui.cb_cities.addItems(cities)

    def getItem(self):
        self.ui.lbl_result.setText("Selected city : " + self.ui.cb_cities.currentText())

        # count = self.ui.cb_cities.count()
        # for index in range(count):
        #     print(self.ui.cb_cities.itemText(index))

    def clearItems(self):
        self.ui.cb_cities.clear()
    
    def selectedChangedIndex(self,index):
        print(index)
    
    def selectedChangedText(self,text):
        print(text)



app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())