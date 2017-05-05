# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wordText = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.wordText.setFont(font)
        self.wordText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wordText.setAutoFillBackground(False)
        self.wordText.setTextFormat(QtCore.Qt.AutoText)
        self.wordText.setAlignment(QtCore.Qt.AlignCenter)
        self.wordText.setObjectName("wordText")
        self.verticalLayout.addWidget(self.wordText)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.translateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.translateButton.setFont(font)
        self.translateButton.setIconSize(QtCore.QSize(16, 16))
        self.translateButton.setObjectName("translateButton")
        self.verticalLayout.addWidget(self.translateButton)
        self.feedbackText = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.feedbackText.setFont(font)
        self.feedbackText.setText("")
        self.feedbackText.setAlignment(QtCore.Qt.AlignCenter)
        self.feedbackText.setObjectName("feedbackText")
        self.verticalLayout.addWidget(self.feedbackText)
        GameWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "MainWindow"))
        self.wordText.setText(_translate("GameWindow", "Word To Translate"))
        self.translateButton.setText(_translate("GameWindow", "Translate!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameWindow = QtWidgets.QMainWindow()
    ui = Ui_GameWindow()
    ui.setupUi(GameWindow)
    GameWindow.show()
    sys.exit(app.exec_())

