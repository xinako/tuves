import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(300, 100, 0, 0)
        self.setWindowTitle("Aplikasi Pendaftaran Posyandu")
        self.setFixedSize(350, 350)
        layout = QtWidgets.QGridLayout()
        self.logform = QtWidgets.QFormLayout()
        self.logform.addRow(QtWidgets.QLabel("Username"), QtWidgets.QLineEdit())
        self.logform.addRow(QtWidgets.QLabel("Password"), QtWidgets.QLineEdit())
        self.logform.addRow(QtWidgets.QPushButton("Login"))
        self.logform.
        layout.addLayout(self.logform)
        self.setLayout(layout)
    def switch(self):
        self.switch_window.emit(self.line_edit.text())

class WindowTwo(QtWidgets.QWidget):
    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(300, 100, 0, 0)
        self.setWindowTitle("Aplikasi Pendaftaran Posyandu")
        self.setFixedSize(350, 350)
        layout = QtWidgets.QGridLayout()
        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)
        self.setLayout(layout)

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(300, 100, 0, 0)
        self.setWindowTitle("Aplikasi Pendaftaran Posyandu")
        self.setFixedSize(350, 350)
        layout = QtWidgets.QGridLayout()
        self.label = QtWidgets.QLabel("Apakah anda anggota baru Posyandu?")
        layout.addWidget(self.label)
        self.button1 = QtWidgets.QPushButton('Ya')
        self.button1.clicked.connect(self.ya1)
        layout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton('Tidak')
        self.button2.clicked.connect(self.no1)
        layout.addWidget(self.button2)
        self.setLayout(layout)
    def no1(self):
        self.switch_window.emit()
    def ya1(self):
        self.switch_window2.emit()


class Controller():
    def __init__(self):
        pass
    def show_login(self):
        self.no1 = Login()
        self.no1.switch_window.connect(self.show_main)
        self.no1.show()
    def register(self):
        self.ya1 = Login()
        self.ya1.switch_window2.connect(self.show_main)
        self.ya1.show()
    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.no1.close()
        self.window.show()
    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
