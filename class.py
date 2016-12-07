# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system reponse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(734, 594)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 691, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 80, 70, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 80, 70, 17))
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.ch = QtGui.QCheckBox(self.centralwidget)
        self.ch.setGeometry(QtCore.QRect(510, 80, 70, 17))
        self.ch.setObjectName(_fromUtf8("ch"))
        self.mass = QtGui.QPlainTextEdit(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(50, 130, 104, 31))
        self.mass.setObjectName(_fromUtf8("mass"))
        self.c = QtGui.QPlainTextEdit(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(510, 140, 104, 31))
        self.c.setObjectName(_fromUtf8("c"))
        self.k = QtGui.QPlainTextEdit(self.centralwidget)
        self.k.setGeometry(QtCore.QRect(270, 130, 101, 31))
        self.k.setObjectName(_fromUtf8("k"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 100, 81, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 110, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 741, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(220, 200, 271, 23))
        self.start.setObjectName(_fromUtf8("start"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "System Resonse", None))
        self.checkBox.setText(_translate("MainWindow", "Mass", None))
        self.checkBox_2.setText(_translate("MainWindow", "Spring", None))
        self.ch.setText(_translate("MainWindow", "Damper", None))
        self.label_2.setText(_translate("MainWindow", "Mass", None))
        self.label_3.setText(_translate("MainWindow", "Spring Constant", None))
        self.label_4.setText(_translate("MainWindow", "Damping Coefficient", None))
        self.start.setText(_translate("MainWindow", "Get System Response", None))

