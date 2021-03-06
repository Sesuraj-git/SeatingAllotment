# -*- coding: utf-8 -*-

# self.Form implementation generated from reading ui file 'updatealert.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class UpdateAlert(QDialog):
    def __init__(self, centralWidget):
        super().__init__()
        self.is_ok = False
        self.centralWidget = centralWidget
        self.Form = QtWidgets.QFrame(self)
        self.setupUi()
        self.exec()

    def setupUi(self):

        self.Form.setObjectName("Form")
        self.Form.resize(437, 255)
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 311, 17))
        self.label.setStyleSheet("font: 75 11pt \"Tibetan Machine Uni\";\n"
                                 "color: rgb(204, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 311, 17))
        self.label_2.setStyleSheet("font: 75 11pt \"Tibetan Machine Uni\";\n"
                                   "color: rgb(204, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.Form)
        self.checkBox.setGeometry(QtCore.QRect(130, 180, 131, 23))
        self.checkBox.setStyleSheet("font: 75 11pt \"Tibetan Machine Uni\";\n"
                                    "color: rgb(204, 0, 0);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggled.connect(lambda: self.box_checked(self.checkBox))
        self.pushButton_3 = QtWidgets.QPushButton(self.Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 220, 89, 25))
        self.pushButton_3.hide()
        self.pushButton_3.setStyleSheet("font: 75 11pt \"Tibetan Machine Uni\";\n"
                                        "background-color: rgb(85, 87, 83);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Form)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 220, 89, 25))
        self.pushButton_4.setStyleSheet("font: 75 11pt \"Tibetan Machine Uni\";\n"
                                        "background-color: rgb(85, 87, 83);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.clicked.connect(self.ok)
        self.pushButton_4.clicked.connect(self.cancel)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def cancel(self):
        self.is_ok = False
        self.deleteLater()

    def ok(self):
        self.deleteLater()
        self.is_ok =True

    def box_checked(self, b):
        if b.isChecked():
            self.pushButton_3.setText("Ok")
            self.pushButton_3.show()
        else:
            self.pushButton_3.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("self.Form", "self.Form"))
        self.label.setText(_translate("self.Form", "You will loose the old Files."))
        self.label_2.setText(_translate("self.Form", "Be very careful while uploading files! "))
        self.checkBox.setText(_translate("self.Form", "I Understand"))

        self.pushButton_4.setText(_translate("self.Form", "Cancel"))
