# coding=utf-8
__author__ = 'brito'

from src import MongoConnect

if __name__ == '__main__':
    client = MongoConnect.MongoConnect()
    train = client.find({'decisao': {'$regex': 'não conheceu dos embargos de declaração'}}, {'decisao':1, '_id':0})

    #train = decisoes[:]

    print train.count()

    for t in train:
        print '- ' + t['decisao'].encode('utf-8')
