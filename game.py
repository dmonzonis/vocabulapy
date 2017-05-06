#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

import sys
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtCore import Qt, QEvent
from dictionary_manager import DictionaryManager
from gui import Ui_GameWindow

class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self, window, dictionaryManager):
        QMainWindow.__init__(self)
        Ui_GameWindow.__init__(self)
        self.setupUi(window)
        qApp.installEventFilter(self)
        self.dManager = dictionaryManager
        self.wordReserve = list(dictionaryManager.dictionary.keys())
        self.word = ""
        self.keyPressed = False

        self.playButton.clicked.connect(self.startGame)
        self.translateButton.clicked.connect(self.processWord)

        self.generateWord()

    def startGame(self):
        if self.endlessCheckBox.isChecked():
            self.endlessMode = True
        else:
            self.endlessMode = False

        self.correctCount = self.failCount = 0
        self.stack.setCurrentIndex(1)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and not self.keyPressed:
            if event.key() == Qt.Key_Return:
                self.keyPressed = True
                self.processWord()
        if event.type() == QEvent.KeyRelease and self.keyPressed:
            if event.key() == Qt.Key_Return:
                self.keyPressed = False
        return super(GameWindow, self).eventFilter(obj, event)

    def generateWord(self):
        if self.wordReserve:
            self.word = choice(self.wordReserve)
            self.wordText.setText(self.word.title())

    def processWord(self):
        text = self.lineEdit.text()
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        if text in self.dManager.dictionary[self.word]:
            self.feedbackText.setText("CORRECT!")
            self.correctCount += 1
            self.okText.setText("""<html><head/><body><p><span style=" color:#07c327;">
                                OK: %s</span></p></body></html>""" % str(self.correctCount))
        else:
            self.feedbackText.setText("Incorrect...")
            self.failCount += 1
            self.failText.setText("""<html><head/><body><p><span style=" color:#bf0808;">
                                Fails: %s</span></p></body></html>""" % str(self.failCount))
        if not self.endlessMode and self.wordReserve:
            self.wordReserve.remove(self.word)
        self.generateWord()


if __name__ == '__main__':
    dManager = DictionaryManager('test.csv')

    app = QApplication(sys.argv)
    window = QMainWindow()
    game = GameWindow(window, dManager)

    window.show()
    sys.exit(app.exec_())
