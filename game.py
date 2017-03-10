import sys
from PyQt4 import QtGui, QtCore
from wordDict import *
from time import sleep


class GameWidget(QtGui.QWidget):

    def __init__(self):
        super(GameWidget, self).__init__()
        self.wordPool = ENG_TO_ES_DICT.keys()
        self.currentWord = self.pullWord()
        self.createUI()

    def createUI(self):
        self.labelWord = QtGui.QLabel(self)
        self.te = QtGui.QLineEdit(self)
        self.labelCorrect = QtGui.QLabel(self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.labelWord)
        vbox.addWidget(self.te)
        vbox.addWidget(self.labelCorrect)

        self.setLayout(vbox)
        self.te.editingFinished.connect(self.validate)
        self.te.setFocus()

        self.labelWord.setText(self.currentWord)

        # Set window parameters and show it
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Vocabula.py')
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Exit Vocabula.py',
                                           "Do you really wanna quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        rect = self.frameGeometry()
        # Get screen center point from the resolution info
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        rect.moveCenter(cp)
        self.move(rect.topLeft())

    def validate(self):
        guess = self.te.text()
        if guess in ENG_TO_ES_DICT[self.currentWord]:
            self.labelCorrect.setText("Correct!")
            #sleep(1)
            self.currentWord = self.pullWord()
            self.labelWord.setText(self.currentWord)
        else:
            self.labelCorrect.setText("Try again")

        self.te.setText('')
        self.te.setFocus()

    def pullWord(self):
        try:
            newWord = choice(self.wordPool)
            self.wordPool.remove(newWord)
            return newWord
        except IndexError:
            return



def main():
    app = QtGui.QApplication(sys.argv)
    widget = GameWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
