#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

import unittest

from vocabulapy.dictionary_manager import DictionaryManager


class TestDictionaryManager(unittest.TestCase):

    def setUp(self):
        self.dictionaryManager = DictionaryManager()

    def test_translate(self):
        enToEsExamples = {
            'olive': 'aceituna',
            'accountant': 'contable',
            'actress': 'actriz',
            'designer': 'diseñador',
            'engineer': 'ingeniero',
            'confidence': 'confianza',
            'disappointment': 'decepción',
            'envy': 'envidia',
            'luggage': 'equipaje',
            'garbage': 'basura',
            'clothing': 'ropa',
            'anger': 'enfado',
            'interview': 'entrevista',
            'training': 'entrenamiento',
            'dishwasher': 'friegaplatos'
        }
        enToEsExamples = {v: k for k, v in enToEsExamples.items()}
        for k, v in enToEsExamples.items():
            # Test English to Spanish and vice versa
            self.assertIn(k, self.dictionaryManager.translate(v, 'en', 'es'))
            self.assertIn(v, self.dictionaryManager.translate(k, 'es', 'en'))


if __name__ == "__main__":
    unittest.main()
