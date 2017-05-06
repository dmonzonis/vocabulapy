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
    def __init__(self, window, dictionaryManager, endlessMode = False):
        QMainWindow.__init__(self)
        Ui_GameWindow.__init__(self)
        self.setupUi(window)
        qApp.installEventFilter(self)
        self.dManager = dictionaryManager
        self.wordReserve = list(dictionaryManager.dictionary.keys())
        self.word = ""
        self.keyPressed = False
        self.endlessMode = endlessMode

        self.translateButton.clicked.connect(self.processWord)

        self.generateWord()

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
        else:
            self.feedbackText.setText("You fail...")
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
