__author__ = 'brito'

# coding=utf-8

from pymongo import MongoClient
import re

if __name__ == '__main__':

    connection = MongoClient('localhost', 27017)
    db = connection['DJs']

    pre = db.preprocessed.find({'$and': [{'decisao': {'$not': re.compile('embargos')}},
                                         {'decisao': {'$not': re.compile('provimento')}},
                                         {'decisao': {'$not': re.compile('procedente')}},
                                         {'decisao': {'$not': re.compile('improcedente')}},
                                         {'decisao': {'$not': re.compile('habeas corpus')}},
                                         {'$or': [{'decisao': re.compile('indefer')},
                                                  {'decisao': re.compile('deneg')},
                                                  {'decisao': re.compile('desprovi')}]}]})

    print str(pre.count()) + ' negativos'

    pos = 0
    neg = 0
    train = 0

    for p in pre:
        result = db.result.find_one({'acordaoId': p['acordaoId']})

        if result is None:
            train = train + 1

        elif result['classificacao'] == 'neg':
            neg = neg + 1

        elif result['classificacao'] == 'pos':
            pos = pos + 1

    print str(train) + ' usado para treinamento'

    print str(pre.count() - train) + ' utilizados para classificacao'

    print str(pos) + ' classificado pos'

    print str(neg) + ' classificado neg'