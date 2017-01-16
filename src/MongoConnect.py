__author__ = 'brito'

from pymongo import MongoClient

class MongoConnect:

    def __init__(self):
        connection = MongoClient('localhost', 27017)
        db = connection['DJs']
        self.collection = db.all

    def find(self, filter, field_selector=None):
        if field_selector == None:
            return self.collection.find(filter, {})
        else:
            return self.collection.find(filter, field_selector)

    def insert(self, data):
        self.collection.insert(data)
