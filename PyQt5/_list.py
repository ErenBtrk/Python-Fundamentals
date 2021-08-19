from PyQt5 import QtWidgets
from PyQt5.QtCore import QMetaEnum
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox
from _listForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #load Students
        self.loadStudents()

    #add Student
        self.ui.btn_add.clicked.connect(self.addStudent)
    
    #edit Studnet
        self.ui.btn_edit.clicked.connect(self.editStudent)

    #delete Student
        self.ui.btn_remove.clicked.connect(self.removeStudent)

    #up
        self.ui.btn_up.clicked.connect(self.upStudent)
    
    #down
        self.ui.btn_down.clicked.connect(self.downStudent)

    #sort
        self.ui.btn_sort.clicked.connect(self.sortStudents)
    
    #exit
        self.ui.btn_exit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.list_Items.addItems(["Ali","Veli","Isa","Musa"])
        self.ui.list_Items.setCurrentRow(0)
    
    def addStudent(self):
        currentIndex = self.ui.list_Items.currentRow()
        text,ok = QInputDialog.getText(self,"New Student","Student Name")
        if ok and text is not None:
            self.ui.list_Items.insertItem(currentIndex,text)

    def editStudent(self):
        index = self.ui.list_Items.currentRow()
        item = self.ui.list_Items.item(index)

        if(item is not None):
            text,ok = QInputDialog.getText(self,"Edit Student","New Student Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.list_Items.currentRow()
        item = self.ui.list_Items.item(index)

        if item is None:
            return
        
        q = QMessageBox.question(self,"Remove Student","Do you want to remove student "+ item.text() + "?",QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.list_Items.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.list_Items.currentRow()
        if(index >= 1):
            item = self.ui.list_Items.takeItem(index)
            self.ui.list_Items.insertItem(index-1,item)
            self.ui.list_Items.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.list_Items.currentRow()
        if(index <= self.ui.list_Items.count() - 1):
            item = self.ui.list_Items.takeItem(index)
            self.ui.list_Items.insertItem(index+1,item)
            self.ui.list_Items.setCurrentItem(item)

    def sortStudents(self):
        self.ui.list_Items.sortItems()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()