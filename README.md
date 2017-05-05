VocabulaPy - Python Vocabulary Game
==============
Small game where you have to translate words from one language to another within a time interval. Right now it only works from English to Spanish, but more languages will be added in the future.

It uses the PyQt5 library for the GUI, and needs an internet connection to generate the translations for the first time. You pass it a CSV file containing words, they are then translated to the target language using the Glosbe API to get the possible solutions, and a dictionary is generated. The player is then prompted words from the dictionary and is asked to translate them. The translation will be successful if the player's input matches one of the possible solutions previously generated.
