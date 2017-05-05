#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

import urllib.request
import csv
import json
import os.path
import sys
import pickle
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtCore import Qt, QEvent
from gui import Ui_GameWindow

# Loads a list of words in English from CSV file and return it
def loadWordList(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        wordList = list(reader)[0]
    # Remove trailing space
    for word in wordList:
        wordList[wordList.index(word)] = word.strip()
    return wordList

# Translates a word using internet API and return list of valid translations
def translate(word):
    translationList = []
    url = "https://glosbe.com/gapi/translate?from=eng&dest=es&format=json&phrase=%s" % word
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    if data['result'] != 'ok':
        print("Error trying to translate word: %s" % word)
        return None
    for translation in data['tuc']:
        if 'phrase' in translation:
            translationList.append(translation['phrase']['text'])
    return translationList

# Creates a dictionary of possible translations for given words (keys)
def createDict(wordList):
    wordDict = dict()
    listLength = len(wordList)
    print("Translating %s words, please be patient" % str(listLength))
    counter = 1
    for word in wordList:
        print("...%s/%s" % (str(counter), str(listLength)))
        translations = translate(word)
        wordDict[word] = translations
        counter += 1
    print("Done!")
    return wordDict

# Creates a game-ready dictionary from a CSV file containing English words, using the Glosbe API
# to translate them if it wasn't previously generated before and saving it for future use, or loading
# the previously generated one if it exists
def loadGameDict(filename):
    if not os.path.exists(filename):
        print("Could not find the word file!")
        return
    dictFilename = filename[:filename.find('.csv')] + '.dict'
    if os.path.exists(dictFilename):
        with open(dictFilename, 'rb') as f:
            return pickle.load(f)
    words = loadWordList(filename)
    wordDict = createDict(words)
    with open(dictFilename, 'wb') as f:
        pickle.dump(wordDict, f, protocol=pickle.HIGHEST_PROTOCOL)
    return wordDict

class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self, window, dictionary):
        QMainWindow.__init__(self)
        Ui_GameWindow.__init__(self)
        self.setupUi(window)
        qApp.installEventFilter(self)
        self.wordDict = dictionary
        self.word = ""
        self.keyPressed = False

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
        self.word = choice(list(wordDict.keys()))
        self.wordText.setText(self.word.title())

    def processWord(self):
        text = self.lineEdit.text()
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        if text in self.wordDict[self.word]:
            self.feedbackText.setText("CORRECT!")
        else:
            self.feedbackText.setText("You fail...")
        self.generateWord()


if __name__ == '__main__':
    wordDict = loadGameDict('qualities.csv')

    app = QApplication(sys.argv)
    window = QMainWindow()
    game = GameWindow(window, wordDict)

    window.show()
    sys.exit(app.exec_())
