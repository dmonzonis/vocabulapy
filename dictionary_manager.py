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
import pickle

class DictionaryManager:
    def __init__(self, filename = None):
        self.dictionary = dict()
        if filename:
            self.load(filename)

    # Loads a list of words in English from CSV file and return it
    def readWordList(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            wordList = list(reader)[0]
        # Remove trailing space
        for word in wordList:
            wordList[wordList.index(word)] = word.strip()
        return wordList

    # Translates a word using internet API and return list of valid translations
    def translate(self, word):
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
    def createDict(self, wordList):
        wordDict = dict()
        listLength = len(wordList)
        print("Translating %s words, please be patient" % str(listLength))
        counter = 1
        for word in wordList:
            print("...%s/%s" % (str(counter), str(listLength)))
            translations = self.translate(word)
            wordDict[word] = translations
            counter += 1
        print("Done!")
        return wordDict

    # Creates a game-ready dictionary from a CSV file containing English words, using the Glosbe API
    # to translate them if it wasn't previously generated before and saving it for future use, or loading
    # the previously generated one if it exists
    def load(self, filename):
        if not os.path.exists(filename):
            print("Could not find the word file!")
            return
        dictFilename = filename[:filename.find('.csv')] + '.dict'
        if os.path.exists(dictFilename):
            with open(dictFilename, 'rb') as f:
                self.dictionary = pickle.load(f)
                return
        words = self.readWordList(filename)
        wordDict = self.createDict(words)
        with open(dictFilename, 'wb') as f:
            pickle.dump(wordDict, f, protocol=pickle.HIGHEST_PROTOCOL)
        self.dictionary = wordDict
