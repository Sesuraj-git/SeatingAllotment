from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCheckBox, QFileDialog, QMessageBox
from readDatabase import read_halls
from final import finalCall


# from alert import CustomDialog

class HallSelect:
    def __init__(self, centralwidget, classes, totalStudents, status):

        self.classes = classes
        self.status = status
        self.centralwidget = centralwidget
        self.totalStudents = totalStudents
        self.select_frame = QtWidgets.QFrame(centralwidget)
        self.upload_button = QtWidgets.QPushButton(self.select_frame)
        self.done_button = QtWidgets.QPushButton(self.select_frame)
        self.listButton = []
        self.halls = []
        self.head_label2 = QtWidgets.QLabel(self.select_frame)
        self.gridLayoutWidget = QtWidgets.QWidget(self.select_frame)
        self.hall_select_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.head_label1 = QtWidgets.QLabel(self.select_frame)
        self.reset_button = QtWidgets.QPushButton(self.select_frame)
        self.setupUi()

    def setupUi(self):
        print("dffks")
        print(self.totalStudents, "stu")
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
        self.head_label1.setText("Select Exam halls from CheckBoxes Or ")
        self.head_label1.show()

        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 84, 941, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.hall_select_layout.setContentsMargins(0, 0, 0, 0)
        self.hall_select_layout.setObjectName("class_select_layout")
        self.gridLayoutWidget.show()

        self.halls = read_halls()
        for i in range(len(self.halls)):
            btn = QCheckBox()
            btn.setStyleSheet("background-image : url(./res/blue.png);")

            font = QtGui.QFont()
            font.setFamily("Tibetan Machine Uni")
            font.setBold(True)
            font.setWeight(75)
            btn.setFont(font)
            if self.status == 1:
                btn.setChecked(True)
            btn.setText(str(self.halls[i][0]))
            btn.toggled.connect(lambda: self.calculate(btn))
            self.listButton.append(btn)
        i = 0
        j = 0
        for btn in self.listButton:
            if i % 5 == 0:
                j = j + 1
                i = 0
            self.hall_select_layout.addWidget(btn, j, i, 1, 1)
            i = i + 1

        self.done_button.setGeometry(QtCore.QRect(868, 494, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)
        self.done_button.setFont(font)
        self.done_button.setObjectName("done_button")
        self.done_button.setText("Done")
        self.done_button.hide()

        if self.status ==1:
            self.calculate(1)
        self.done_button.clicked.connect(self.doneButtonClicked)

        self.head_label2.setGeometry(QtCore.QRect(408, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setBold(True)
        font.setWeight(75)
        self.head_label2.setFont(font)
        self.head_label2.setObjectName("head_label2")
        self.head_label2.setText(" to Upload a .xlsx file")
        self.head_label2.show()

        self.upload_button.setGeometry(QtCore.QRect(322, 51, 91, 25))
        self.upload_button.setObjectName("upload_button")
        self.upload_button.setText("Click here")
        self.upload_button.show()
        self.upload_button.setStyleSheet("color : blue")
        self.upload_button.clicked.connect(self.uploadButtonClicked)

    def calculate(self, b):
        halls_selected = []
        total = 0
        for btn in self.listButton:
            if btn.isChecked():

                index = self.listButton.index(btn)
                halls_selected.append(self.halls[index])
                val = int(self.halls[index][1]) * int(self.halls[index][2])
                total = total + val
                if self.totalStudents <= total:
                    print(total, self.totalStudents)
                    self.done_button.show()
                else:
                    self.done_button.hide()

        print(halls_selected, total, self.totalStudents, "halls")
        self.totalSeats = total

        return halls_selected

    def resetButtonClicked(self):
        for btn in self.listButton:
            btn.setChecked(False)

    def doneButtonClicked(self):
        self.halls = self.calculate(1)
        self.select_frame.deleteLater()
        print("Final indexes", self.halls, "total Students", self.totalStudents, "total Seats", self.totalSeats)

        self.showDialog()

        # finalCall(classes=self.classes,halls=self.halls, centralwidget=self.centralwidget)

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Select The OutputFile Location")
        msgBox.setWindowTitle("Message")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())
        location = QFileDialog.getExistingDirectory()

        finalCall(classes=self.classes, halls=self.halls, outFileLoc=location)
