from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _tableForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btn_save.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(),item.column(),item.text())

    def saveProduct(self):
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()

        if(name and price is not None):
            rowCount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1,QTableWidgetItem(price))

    def loadProducts(self):

        products = [
            {"name" : "Samsung s5","price" : 2000},
            {"name" : "Samsung s6","price" : 3000},
            {"name" : "Samsung s7","price" : 4000},
            {"name" : "Samsung s8","price" : 5000},
            {"name" : "IPhone 7","price" : 6000}
        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(product["name"]))
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(product["price"])))
            rowIndex+=1

        
        
        

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())