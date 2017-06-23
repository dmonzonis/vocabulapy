#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VocabulaPy

Small python game where you translate words.

author: Daniel Monzonis
website: github.com/monzo94
"""

from vocabulapy.dictionary_manager import DictionaryManager


def test_translate():
    dictionaryManager = DictionaryManager()
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
        'dishwasher': 'friegaplatos',
    }
    enToEsExamples = {v: k for k, v in enToEsExamples.items()}
    for k, v in enToEsExamples.items():
        # Test English to Spanish and vice versa
        assert(k in dictionaryManager.translate(v, 'en', 'es'))
        assert(v in dictionaryManager.translate(k, 'es', 'en'))
