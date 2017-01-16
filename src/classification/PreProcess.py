# coding=utf-8

from nltk.corpus import stopwords
import re

class PreProcess():
    def remove_stop_words(self, word_list):
        return [word for word in word_list if word not in stopwords.words('portuguese')]

    def remove_given_stop_words(self, word_list, stop_word_list):
        return [word for word in word_list if word.encode('utf-8') not in stop_word_list]

    def lower(self, phrase):
        return phrase.lower()

    def remove_date(self, phrase):
        return re.sub(r'([0-9]{2}|[0-9]).([0-9]{2}|[0-9]).([0-9]{4}|[0-9]{2})(.|)', '', phrase)

    def remove_punctuation(self, phrase):
        return re.sub(r'(,|-|\.)', '', phrase)