import urllib.request
import csv
import json
import os.path

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

words = loadWordList("qualities.csv")
d = createDict(words)
print(d)
