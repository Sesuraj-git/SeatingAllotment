from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCheckBox, QFileDialog

from dialogHalls import Ui_DialogHalls
from readDatabase import read_classes
from hall_select import HallSelect

global classFile


class ClassSelect:
    def __init__(self, centralWidget, directory, status):

        self.classes = []
        self.status = status
        self.directory = directory
        self.centralWidget = centralWidget
        self.totalStudents = 0
        self.select_frame = QtWidgets.QFrame(centralWidget)
        self.done_button = QtWidgets.QPushButton(self.select_frame)
        self.listButton = []
        self.gridLayoutWidget = QtWidgets.QWidget(self.select_frame)
        self.class_select_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.head_label1 = QtWidgets.QLabel(self.select_frame)
        self.reset_button = QtWidgets.QPushButton(self.select_frame)
        self.setupUi()

    def setupUi(self):
        print("diffs")
        self.select_frame.setGeometry(QtCore.QRect(10, 41, 1021, 521))
        self.select_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_frame.setObjectName("home_frame")
        self.select_frame.setStyleSheet("background-image : url(./res/dark.jpeg);")

        self.select_frame.show()
        self.reset_button.setGeometry(QtCore.QRect(28, 494, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setText("Reset")
        self.reset_button.show()
        self.reset_button.clicked.connect(self.resetButtonClicked)

        self.head_label1.setGeometry(QtCore.QRect(25, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)
        self.head_label1.setFont(font)
        self.head_label1.setObjectName("head_label1")
        self.head_label1.setText("Select classes from CheckBoxes ")
        self.head_label1.show()

        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 84, 941, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.class_select_layout.setContentsMargins(0, 0, 0, 0)
        self.class_select_layout.setObjectName("class_select_layout")
        self.gridLayoutWidget.show()

        self.classes = read_classes(self.directory)
        self.checkBox()
        self.status = 1

        self.done_button.setGeometry(QtCore.QRect(868, 494, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)
        self.done_button.setFont(font)
        self.done_button.setObjectName("done_button")
        self.done_button.setText("Done")
        self.done_button.show()

        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)

        self.done_button.clicked.connect(self.doneButtonClicked)

    def checkBox(self):
        print("if")
        for i in range(len(self.classes)):
            btn = QCheckBox()
            if self.status == 1:
                btn.setChecked(True)
            btn.setStyleSheet("background-image : url(./res/blue.png);")

            font = QtGui.QFont()
            font.setFamily("Tibetan Machine Uni")
            font.setBold(True)
            font.setWeight(75)
            btn.setFont(font)

            btn.setText(str(self.classes[i][0]))
            btn.toggled.connect(lambda: self.calculate(btn))
            self.listButton.append(btn)
        i = 0
        j = 0
        for btn in self.listButton:
            if i % 5 == 0:
                j = j + 1
                i = 0
            self.class_select_layout.addWidget(btn, j, i, 1, 1)
            i = i + 1

    def calculate(self, b):
        classes_selected = []
        total = 0
        print(b)
        for btn in self.listButton:
            if btn.isChecked():
                index = self.listButton.index(btn)
                classes_selected.append(self.classes[index])
                val = self.classes[index][1]
                total = total + val

        print(classes_selected, total)
        self.totalStudents = total

        return classes_selected

    def resetButtonClicked(self):
        for btn in self.listButton:
            btn.setChecked(False)

    def doneButtonClicked(self):
        self.classes = self.calculate(1)
        self.select_frame.deleteLater()
        print("indexes", self.classes)
        print(self.totalStudents, "here")
        Ui_DialogHalls(self.centralWidget, classes=self.classes, totalStudents=self.totalStudents)
        # HallSelect(self.centralWidget, classes=self.classes, totalStudents=self.totalStudents)
