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

TRANS_URL = "https://glosbe.com/gapi/"\
        "translate?from={}&dest={}&format=json&phrase={}"


class DictionaryManager:
    def __init__(self, filename=None):
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

    # Translates a word using internet API and return list of
    # valid translations
    def translate(self, word, sourceLang, destLang):
        translationList = []
        url = TRANS_URL.format(sourceLang, destLang, word)
        response = urllib.request.urlopen(url).read()
        data = json.loads(response)
        if data['result'] != 'ok':
            print("Error trying to translate word: %s" % word)
            return None
        for translation in data['tuc']:
            # Translations have a 'phrase' key
            if 'phrase' in translation:
                translationList.append(translation['phrase']['text'])
        return translationList

    # Creates a dictionary of possible translations for given words (keys)
    def createDict(self, wordList, sourceLang, destLang):
        wordDict = dict()
        listLength = len(wordList)
        print("Translating %s words, please be patient" % str(listLength))
        counter = 1
        for word in wordList:
            print("...%s/%s" % (str(counter), str(listLength)))
            translations = self.translate(word, sourceLang, destLang)
            wordDict[word] = translations
            counter += 1
        print("Done!")
        return wordDict

    # Creates a game-ready dictionary from a CSV file containing English
    # words, using the Glosbe API to translate them if it wasn't
    # previously generated before and saving it for future use, or loading
    # the previously generated one if it exists
    def load(self, filename, sourceLang, destLang):
        if not os.path.exists(filename):
            print("Could not find the word file!")
            return
        dictFilename = filename[:filename.find('.csv')] + '.dict'
        # If dictionary already exists, use it
        if os.path.exists(dictFilename):
            with open(dictFilename, 'rb') as f:
                self.dictionary = pickle.load(f)
                return
        # Dictionary doesn't exist, create a new one
        words = self.readWordList(filename)
        wordDict = self.createDict(words, sourceLang, destLang)
        # Save it to a file for future use
        with open(dictFilename, 'wb') as f:
            pickle.dump(wordDict, f, protocol=pickle.HIGHEST_PROTOCOL)

        self.dictionary = wordDict
