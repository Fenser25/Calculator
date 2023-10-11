from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

app = QApplication([])
mainWin = QWidget()
mainWin.resize(1000, 600)
Vline = QVBoxLayout()
text = QLabel()
text.setText('')
Vline.addWidget(text, alignment = Qt.AlignCenter)



Hline1 = QHBoxLayout()


bttn1 = QPushButton('1')
bttn2 = QPushButton('2')
bttn3 = QPushButton('3')

Hline1.addWidget(bttn1, alignment = Qt.AlignCenter)
Hline1.addWidget(bttn2, alignment = Qt.AlignCenter)
Hline1.addWidget(bttn3, alignment = Qt.AlignCenter)




Hline2 = QHBoxLayout()


bttn4 = QPushButton('4')
bttn5 = QPushButton('5')
bttn6 = QPushButton('6')
Hline2.addWidget(bttn4, alignment = Qt.AlignCenter)
Hline2.addWidget(bttn5, alignment = Qt.AlignCenter)
Hline2.addWidget(bttn6, alignment = Qt.AlignCenter)


Hline3 = QHBoxLayout()


bttn7 = QPushButton('7')
bttn8 = QPushButton('8')
bttn9 = QPushButton('9')
Hline3.addWidget(bttn7, alignment = Qt.AlignCenter)
Hline3.addWidget(bttn8, alignment = Qt.AlignCenter)
Hline3.addWidget(bttn9, alignment = Qt.AlignCenter)


Hline4 = QHBoxLayout()
bttn0 = QPushButton('0')
bttn_plus = QPushButton('+')
bttn_minus = QPushButton('-')

Hline4.addWidget(bttn0, alignment = Qt.AlignCenter)
Hline4.addWidget(bttn_plus, alignment = Qt.AlignCenter)
Hline4.addWidget(bttn_minus, alignment = Qt.AlignCenter)


Hline5 = QHBoxLayout()


bttn_multiply = QPushButton('*')
bttn_devide = QPushButton('/')
bttn_equel = QPushButton('=')
Hline5.addWidget(bttn_multiply, alignment = Qt.AlignCenter)
Hline5.addWidget(bttn_devide, alignment = Qt.AlignCenter)
Hline5.addWidget(bttn_equel, alignment = Qt.AlignCenter)


Hline6 = QHBoxLayout()
bttn_C = QPushButton('C')
Hline6.addWidget(bttn_C, alignment = Qt.AlignCenter)








Vline.addLayout(Hline1)
Vline.addLayout(Hline2)
Vline.addLayout(Hline3)
Vline.addLayout(Hline4)
Vline.addLayout(Hline5)
Vline.addLayout(Hline6)


def bttn1_func():
    text.setText(text.text() + '1')
bttn1.clicked.connect(bttn1_func)
def bttn_c_func():
    text.setText('')
bttn_C.clicked.connect(bttn_c_func)
def bttn2_func():
    text.setText(text.text() + '2')
bttn2.clicked.connect(bttn2_func)
def bttn3_func():
    text.setText(text.text() + '3')
bttn3.clicked.connect(bttn3_func)
def bttn4_func():
    text.setText(text.text() + '4')
bttn4.clicked.connect(bttn4_func)
def bttn5_func():
    text.setText(text.text() + '5')
bttn5.clicked.connect(bttn5_func)
def bttn6_func():
    text.setText(text.text() + '6')
bttn6.clicked.connect(bttn6_func)
def bttn7_func():
    text.setText(text.text() + '7')
bttn7.clicked.connect(bttn7_func)
def bttn8_func():
    text.setText(text.text() + '8')
bttn8.clicked.connect(bttn8_func)
def bttn9_func():
    text.setText(text.text() + '9')
bttn9.clicked.connect(bttn9_func)
def bttn0_func():
    text.setText(text.text() + '0')
bttn0.clicked.connect(bttn0_func)
def bttn_plus_func():
    text.setText(text.text() + ' + ')
bttn_plus.clicked.connect(bttn_plus_func)
def bttn_minus_func():
    text.setText(text.text() + ' - ')
bttn_minus.clicked.connect(bttn_minus_func)
def bttn_devide_func():
    text.setText(text.text() + ' / ')
bttn_devide.clicked.connect(bttn_devide_func)
def bttn_multiply_func():
    text.setText(text.text() + ' * ')
bttn_multiply.clicked.connect(bttn_multiply_func)



def bttn_equel_func():
    x = text.text().split()
    list_x = list(x)
    znak = list_x[1]
    if znak == '+':
        text.setText(str(int(list_x[0]) + int(list_x[2])))
    if znak == '-':
        text.setText(str(int(list_x[0]) - int(list_x[2])))
    if znak == '/':
        text.setText(str(int(list_x[0]) / int(list_x[2])))
    if znak == '*':
        text.setText(str(int(list_x[0]) * int(list_x[2])))

bttn_equel.clicked.connect(bttn_equel_func)









mainWin.setLayout(Vline)
mainWin.show()
app.exec_()





