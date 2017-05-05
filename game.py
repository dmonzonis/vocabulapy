import urllib.request
import csv
import json
import os.path
import pickle

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

d = loadGameDict("qualities.csv")
print(d)
