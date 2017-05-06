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
        GameWindow.resize(685, 498)
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setGeometry(QtCore.QRect(9, 0, 671, 491))
        self.stack.setObjectName("stack")
        self.menu_state = QtWidgets.QWidget()
        self.menu_state.setObjectName("menu_state")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.menu_state)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 671, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleText = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titleText.setFont(font)
        self.titleText.setAlignment(QtCore.Qt.AlignCenter)
        self.titleText.setObjectName("titleText")
        self.verticalLayout_2.addWidget(self.titleText)
        self.authorText = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.authorText.setAlignment(QtCore.Qt.AlignCenter)
        self.authorText.setObjectName("authorText")
        self.verticalLayout_2.addWidget(self.authorText)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.menu_state)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 671, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.endlessCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.endlessCheckBox.setObjectName("endlessCheckBox")
        self.horizontalLayout.addWidget(self.endlessCheckBox)
        self.wordFileList = QtWidgets.QListWidget(self.menu_state)
        self.wordFileList.setGeometry(QtCore.QRect(0, 150, 256, 331))
        self.wordFileList.setObjectName("wordFileList")
        item = QtWidgets.QListWidgetItem()
        self.wordFileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wordFileList.addItem(item)
        self.playButton = QtWidgets.QPushButton(self.menu_state)
        self.playButton.setGeometry(QtCore.QRect(340, 240, 241, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setObjectName("playButton")
        self.stack.addWidget(self.menu_state)
        self.game_state = QtWidgets.QWidget()
        self.game_state.setObjectName("game_state")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.game_state)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 671, 351))
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.game_state)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 370, 671, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okText = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.okText.setFont(font)
        self.okText.setLineWidth(1)
        self.okText.setTextFormat(QtCore.Qt.RichText)
        self.okText.setAlignment(QtCore.Qt.AlignCenter)
        self.okText.setObjectName("okText")
        self.horizontalLayout_2.addWidget(self.okText)
        self.failText = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.failText.setFont(font)
        self.failText.setTextFormat(QtCore.Qt.RichText)
        self.failText.setAlignment(QtCore.Qt.AlignCenter)
        self.failText.setObjectName("failText")
        self.horizontalLayout_2.addWidget(self.failText)
        self.wordText.raise_()
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.stack.addWidget(self.game_state)
        GameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "MainWindow"))
        self.titleText.setText(_translate("GameWindow", "VocabulaPy"))
        self.authorText.setText(_translate("GameWindow", "by Daniel Monzonís"))
        self.endlessCheckBox.setText(_translate("GameWindow", "Endless Mode"))
        __sortingEnabled = self.wordFileList.isSortingEnabled()
        self.wordFileList.setSortingEnabled(False)
        item = self.wordFileList.item(0)
        item.setText(_translate("GameWindow", "Basic Words"))
        item = self.wordFileList.item(1)
        item.setText(_translate("GameWindow", "Qualities"))
        self.wordFileList.setSortingEnabled(__sortingEnabled)
        self.playButton.setText(_translate("GameWindow", "Play!"))
        self.wordText.setText(_translate("GameWindow", "Word To Translate"))
        self.translateButton.setText(_translate("GameWindow", "Translate!"))
        self.okText.setText(_translate("GameWindow", "<html><head/><body><p><span style=\" color:#07c327;\">OK: 0</span></p></body></html>"))
        self.failText.setText(_translate("GameWindow", "<html><head/><body><p><span style=\" color:#bf0808;\">Fails: 0</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameWindow = QtWidgets.QMainWindow()
    ui = Ui_GameWindow()
    ui.setupUi(GameWindow)
    GameWindow.show()
    sys.exit(app.exec_())

