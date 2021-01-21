from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import math
ui,_ = loadUiType('cal.ui')

class MainApp(QMainWindow,ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handl_button()

    def handl_button(self):
        self.pushButton_10.clicked.connect(self.number_0)
        self.pushButton.clicked.connect(self.number_7)
        self.pushButton_2.clicked.connect(self.number_8)
        self.pushButton_3.clicked.connect(self.number_9)
        self.pushButton_4.clicked.connect(self.number_5)
        self.pushButton_5.clicked.connect(self.number_4)
        self.pushButton_6.clicked.connect(self.number_6)
        self.pushButton_7.clicked.connect(self.number_1)
        self.pushButton_8.clicked.connect(self.number_2)
        self.pushButton_9.clicked.connect(self.number_3)
        self.pushButton_16.clicked.connect(self.addition)
        self.pushButton_14.clicked.connect(self.subtraction)
        self.pushButton_15.clicked.connect(self.multiplication)
        self.pushButton_13.clicked.connect(self.division)
        self.pushButton_11.clicked.connect(self.equal)
        self.pushButton_12.clicked.connect(self.points)
        self.pushButton_18.clicked.connect(self.clear_fun)
        self.pushButton_17.clicked.connect(self.delet_fun)
        self.pushButton_19.clicked.connect(self.power)
        self.pushButton_21.clicked.connect(self.sinus)
    def number_0(self):
       text=self.lineEdit.text()
       self.lineEdit.setText(text + '0')

    def number_7(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '7')

    def number_8(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '8')
    def number_9(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '9')

    def number_5(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '5')

    def number_4(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '4')

    def number_6(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '6')

    def number_3(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '3')

    def number_2(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '2')

    def points(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '.')
    def number_1(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '1')
    def addition(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '+')
    def subtraction(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '-')
    def multiplication(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '*')
    def division(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '/')
    def equal(self):
        text=self.lineEdit.text()
        eql=eval(text)
        self.lineEdit.setText(str(eql))
    def power(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '**')
    def sinus(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(  'sin'+'(' + text+ ')')

        #text=int(text)
        #a = math.sin(text)
        #self.lineEdit.setText( a)
    def clear_fun(self):
        self.lineEdit.setText('')

    def delet_fun(self):
        text = self.lineEdit.text()
        #fun=text.split()
        part=(text[-1])
        new_p=text.replace(part,'')
        self.lineEdit.setText(str(new_p))
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ ==  '__main__':
    main()
