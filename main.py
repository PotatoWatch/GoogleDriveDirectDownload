from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyperclip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setFixedSize(422, 361)
        MainWindow.setWindowTitle('Google Drive Direct Download Link Maker')
        MainWindow.setWindowIcon(QtGui.QIcon('Assets/link-clear.png'))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 381, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.OutputLine = QtWidgets.QLineEdit(self.centralwidget)
        self.OutputLine.setGeometry(QtCore.QRect(20, 230, 381, 22))
        self.OutputLine.setObjectName("OutputLine")
        self.InputLine = QtWidgets.QLineEdit(self.centralwidget)
        self.InputLine.setGeometry(QtCore.QRect(20, 110, 381, 22))
        self.InputLine.setObjectName("InputLine")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.translate_url)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Google Drive Direct Link Creator"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Output"))
        self.label_2.setText(_translate("MainWindow", "Input"))
        self.label_3.setText(_translate("MainWindow", "Google Drive Direct Download Link Creator"))

    def translate_url(self):
        input_value = self.InputLine.text()
        splited_value = input_value.split("https://drive.google.com/file/d/")
        splited = splited_value[1].split("/view?usp=sharing")
        output_val = splited[0]
        output_str = f"https://drive.google.com/uc?id={output_val}&export=download"
        self.OutputLine.setText(output_str)
        pyperclip.copy(output_str)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
