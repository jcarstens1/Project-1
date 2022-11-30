# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectview.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Submit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_Button.setGeometry(QtCore.QRect(70, 560, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Submit_Button.setFont(font)
        self.Submit_Button.setStyleSheet("background-color:rgb(255, 223, 92);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 14pt \"Rockwell Extra Bold\";")
        self.Submit_Button.setObjectName("Submit_Button")
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(300, 560, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Clear_Button.setFont(font)
        self.Clear_Button.setStyleSheet("background-color:rgb(255, 223, 92);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 14pt \"Rockwell Extra Bold\";")
        self.Clear_Button.setObjectName("Clear_Button")
        self.Radio_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_10.setEnabled(True)
        self.Radio_10.setGeometry(QtCore.QRect(100, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Radio_10.setFont(font)
        self.Radio_10.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";")
        self.Radio_10.setChecked(True)
        self.Radio_10.setObjectName("Radio_10")
        self.Radio_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_15.setEnabled(True)
        self.Radio_15.setGeometry(QtCore.QRect(170, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Radio_15.setFont(font)
        self.Radio_15.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";")
        self.Radio_15.setObjectName("Radio_15")
        self.Radio_20 = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_20.setEnabled(True)
        self.Radio_20.setGeometry(QtCore.QRect(240, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Radio_20.setFont(font)
        self.Radio_20.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";")
        self.Radio_20.setObjectName("Radio_20")
        self.Food_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Food_Entry.setGeometry(QtCore.QRect(110, 100, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Food_Entry.setFont(font)
        self.Food_Entry.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Food_Entry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Food_Entry.setStyleSheet("background-color: rgb(243, 255, 199);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 13pt \"Rockwell Extra Bold\"")
        self.Food_Entry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Food_Entry.setText("")
        self.Food_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Food_Entry.setObjectName("Food_Entry")
        self.Drink_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Drink_Entry.setGeometry(QtCore.QRect(110, 160, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Drink_Entry.setFont(font)
        self.Drink_Entry.setStyleSheet("background-color: rgb(243, 255, 199);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 13pt \"Rockwell Extra Bold\"")
        self.Drink_Entry.setText("")
        self.Drink_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Drink_Entry.setObjectName("Drink_Entry")
        self.Dessert_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Dessert_Entry.setGeometry(QtCore.QRect(110, 220, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Dessert_Entry.setFont(font)
        self.Dessert_Entry.setStyleSheet("background-color: rgb(243, 255, 199);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 13pt \"Rockwell Extra Bold\";\n"
"")
        self.Dessert_Entry.setText("")
        self.Dessert_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Dessert_Entry.setObjectName("Dessert_Entry")
        self.Bill_Calc_Label = QtWidgets.QLabel(self.centralwidget)
        self.Bill_Calc_Label.setGeometry(QtCore.QRect(10, 20, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(10)
        self.Bill_Calc_Label.setFont(font)
        self.Bill_Calc_Label.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Bill_Calc_Label.setScaledContents(False)
        self.Bill_Calc_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Bill_Calc_Label.setObjectName("Bill_Calc_Label")
        self.Food_Label = QtWidgets.QLabel(self.centralwidget)
        self.Food_Label.setGeometry(QtCore.QRect(20, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Food_Label.setFont(font)
        self.Food_Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Food_Label.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Food_Label.setWordWrap(True)
        self.Food_Label.setObjectName("Food_Label")
        self.Drink_Label = QtWidgets.QLabel(self.centralwidget)
        self.Drink_Label.setGeometry(QtCore.QRect(20, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Drink_Label.setFont(font)
        self.Drink_Label.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Drink_Label.setObjectName("Drink_Label")
        self.Dessert_Label = QtWidgets.QLabel(self.centralwidget)
        self.Dessert_Label.setGeometry(QtCore.QRect(20, 220, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Dessert_Label.setFont(font)
        self.Dessert_Label.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Dessert_Label.setObjectName("Dessert_Label")
        self.Tip_Label = QtWidgets.QLabel(self.centralwidget)
        self.Tip_Label.setGeometry(QtCore.QRect(20, 280, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Tip_Label.setFont(font)
        self.Tip_Label.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Tip_Label.setObjectName("Tip_Label")
        self.Summary_Label = QtWidgets.QLabel(self.centralwidget)
        self.Summary_Label.setGeometry(QtCore.QRect(70, 330, 341, 201))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Summary_Label.setFont(font)
        self.Summary_Label.setStyleSheet("font: 81 13pt \"Rockwell Extra Bold\"")
        self.Summary_Label.setText("")
        self.Summary_Label.setTextFormat(QtCore.Qt.AutoText)
        self.Summary_Label.setScaledContents(False)
        self.Summary_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Summary_Label.setWordWrap(False)
        self.Summary_Label.setObjectName("Summary_Label")
        self.Radio_Custom = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_Custom.setGeometry(QtCore.QRect(310, 280, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Radio_Custom.setFont(font)
        self.Radio_Custom.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";")
        self.Radio_Custom.setObjectName("Radio_Custom")
        self.Custom_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Custom_Entry.setGeometry(QtCore.QRect(420, 280, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Custom_Entry.setFont(font)
        self.Custom_Entry.setStyleSheet("background-color: rgb(243, 255, 199);\n"
"color: black;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color:rgb(0, 0, 0);\n"
"font: 81 13pt \"Rockwell Extra Bold\"")
        self.Custom_Entry.setText("")
        self.Custom_Entry.setMaxLength(4)
        self.Custom_Entry.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Custom_Entry.setReadOnly(False)
        self.Custom_Entry.setClearButtonEnabled(False)
        self.Custom_Entry.setObjectName("Custom_Entry")
        self.Split_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Split_Checkbox.setGeometry(QtCore.QRect(20, 330, 121, 31))
        self.Split_Checkbox.setStyleSheet("font: 81 14pt \"Rockwell Extra Bold\";")
        self.Split_Checkbox.setObjectName("Split_Checkbox")
        self.Split_Entry = QtWidgets.QSpinBox(self.centralwidget)
        self.Split_Entry.setGeometry(QtCore.QRect(150, 330, 51, 31))
        self.Split_Entry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(243, 255, 199);\n"
"font: 81 12pt \"Rockwell Extra Bold\";")
        self.Split_Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Split_Entry.setReadOnly(False)
        self.Split_Entry.setMinimum(1)
        self.Split_Entry.setObjectName("Split_Entry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bill Calculator"))
        self.Submit_Button.setText(_translate("MainWindow", "SUBMIT"))
        self.Clear_Button.setText(_translate("MainWindow", "CLEAR"))
        self.Radio_10.setText(_translate("MainWindow", "10%"))
        self.Radio_15.setText(_translate("MainWindow", "15%"))
        self.Radio_20.setText(_translate("MainWindow", "20%"))
        self.Bill_Calc_Label.setText(_translate("MainWindow", "BILL CALCULATOR"))
        self.Food_Label.setText(_translate("MainWindow", "Food"))
        self.Drink_Label.setText(_translate("MainWindow", "Drink"))
        self.Dessert_Label.setText(_translate("MainWindow", "Dessert"))
        self.Tip_Label.setText(_translate("MainWindow", "Tip"))
        self.Radio_Custom.setText(_translate("MainWindow", "Custom $"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
