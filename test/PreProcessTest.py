# coding=utf-8
__author__ = 'brito'

import unittest

from src.classification import PreProcess


class PreProcessTest(unittest.TestCase):
    """Test for PreProcess class"""

    def test_default_stop_words(self):
        words = PreProcess.PreProcess().remove_stop_words('o amor é lindo'.split(' '))
        self.assertEquals(['amor', 'é', 'lindo'], words)

    def test_given_stop_words(self):
        words = PreProcess.PreProcess().remove_given_stop_words('Ministro Jose Carlos'.split(' '), ['Ministro', 'Jose'])
        self.assertEquals(['Carlos'], words)

    def test_lower(self):
        phrase = PreProcess.PreProcess().lower('Rafael')
        self.assertEqual('rafael', phrase)

    def test_remove_date(self):
        phrase = PreProcess.PreProcess().remove_date('23.04.2002')
        self.assertEqual('', phrase)