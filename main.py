#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from vocabulapy.dictionary_manager import DictionaryManager
from vocabulapy.game import GameWindow

if __name__ == '__main__':
    dManager = DictionaryManager()

    app = QApplication(sys.argv)
    window = QMainWindow()
    game = GameWindow(window, dManager)

    window.show()
    sys.exit(app.exec_())
