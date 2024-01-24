"""
PyQT5 - Is a toolkit developed in C++ and is used by many programs
to create GUI applications (Graphic Interface). Have many other functions like
DB acess, threads, network communication, etc...
pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton("Texto do botão")
        self.btn.setStyleSheet('font-size: 40px;')
        # line 0, columm 0, rolspanns the button occup 1, collumms the button will occupy 1
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.action)

        self.setCentralWidget(self.cw)

    def action(self):
        print('Something... ')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
