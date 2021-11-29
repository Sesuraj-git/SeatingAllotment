from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog

from hall_select import HallSelect


class Ui_DialogHalls(QDialog):
    def __init__(self, centralWidget, classes, totalStudents):
        super().__init__()
        self.classes = classes
        self.totalStudents = totalStudents
        self.centralWidget = centralWidget
        self.setupUi()
        self.exec()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(566, 193)
        self.setStyleSheet("background-color: rgb(20, 24, 34);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 291, 341))
        self.frame.setStyleSheet("font: 75 11pt \"Uroob\";\n"
                                 "background-color: rgb(239, 41, 41);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 50, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 50 15pt \"Ubuntu Condensed\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 241, 31))
        self.label_2.setStyleSheet("font: 75 20pt \"Ubuntu Condensed\";\n"
                                   "color: rgb(204, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 100, 89, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(239, 41, 41);\n"
                                        "border-color: rgb(115, 210, 22);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2.clicked.connect(self.select)

    def select(self):
        self.deleteLater()
        HallSelect(self.centralWidget, classes=self.classes, totalStudents=self.totalStudents, status=0)

    def upload(self):
        self.deleteLater()
        directory = QFileDialog.getOpenFileName()
        directory = directory[0]

        HallSelect(self.centralWidget, classes=self.classes, totalStudents=self.totalStudents, status=1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Upload ExamHalls file as .txt file"))
        self.pushButton.setText(_translate("Dialog", "Upload"))
        self.label_2.setText(_translate("Dialog", "Select from CheckBoxes"))
        self.pushButton_2.setText(_translate("Dialog", "Select"))
