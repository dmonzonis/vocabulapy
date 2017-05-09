#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

import sys
import os
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtCore import Qt, QEvent
from dictionary_manager import DictionaryManager
from gui import Ui_GameWindow


# Format filename for printing, ex. "basic_words.csv" to "Basic Words"
def formatFilename(filename):
    return filename[:filename.find('.')].replace('_', ' ').title()


class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self, window, dictionaryManager):
        QMainWindow.__init__(self)
        Ui_GameWindow.__init__(self)
        self.setupUi(window)
        qApp.installEventFilter(self)
        self.dManager = dictionaryManager
        self.word = ""
        self.keyPressed = False
        self.gameRunning = False

        # Find all .csv files in the directory
        self.fileList = []
        for file in os.listdir(os.getcwd()):
            if file.endswith(".csv"):
                self.fileList.append(file)
        for filename in self.fileList:
            self.wordFileList.addItem(formatFilename(filename))

        self.playButton.clicked.connect(self.startGame)
        self.translateButton.clicked.connect(self.processWord)

    def getLanguage(self):
        if self.sourceLangBox.currentIndex() == 1:
            source = 'es'
        else:
            source = 'en'  # Default

        if self.destLangBox.currentIndex() == 1:
            dest = 'en'
        else:
            dest = 'es'  # Default

        return source, dest

    def startGame(self):
        self.gameRunning = True
        self.dManager.load(self.fileList[self.wordFileList.currentRow()],
                           *self.getLanguage())
        self.wordReserve = list(self.dManager.dictionary.keys())
        if self.endlessCheckBox.isChecked():
            self.endlessMode = True
        else:
            self.endlessMode = False

        self.correctCount = self.failCount = 0
        self.stack.setCurrentIndex(1)
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
        else:
            self.lineEdit.setEnabled(False)
            self.feedbackText.setText("Finished!")
            self.gameRunning = False

    def processWord(self):
        if not self.gameRunning:
            return
        text = self.lineEdit.text()
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        if text in self.dManager.dictionary[self.word]:
            self.feedbackText.setText("Correct!")
            self.correctCount += 1
            self.okText.setText("""<html><head/><body><p>
                                <span style=" color:#07c327;">
                                OK: %s
                                </span></p></body></html>"""
                                % str(self.correctCount))
        else:
            self.feedbackText.setText("Incorrect...")
            self.failCount += 1
            self.failText.setText("""<html><head/><body><p>
                                  <span style=" color:#bf0808;">
                                  Fails: %s
                                  </span></p></body></html>"""
                                  % str(self.failCount))
        if not self.endlessMode and self.wordReserve:
            self.wordReserve.remove(self.word)
        self.generateWord()


if __name__ == '__main__':
    dManager = DictionaryManager()

    app = QApplication(sys.argv)
    window = QMainWindow()
    game = GameWindow(window, dManager)

    window.show()
    sys.exit(app.exec_())
