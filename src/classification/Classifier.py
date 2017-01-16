# coding=utf-8

__author__ = 'brito'

from textblob.classifiers import NaiveBayesClassifier
from pymongo import MongoClient

if __name__ == '__main__':

    connection = MongoClient('localhost', 27017)
    db = connection['DJs']

    decisoes_train = db.trained.find({"$or": [{"classificao": "neg"}, {"classificao": "pos"}]})

    train = []

    print 'populando lista de treinamento'

    for decisao in decisoes_train:
        t = (decisao['decisao'].split(' '), decisao['classificao'].encode('utf-8'))
        #print t
        train.append(t)

    print 'iniciando treinamento'

    cl = NaiveBayesClassifier(train)

    decisoes_test = db.test.find({})

    print 'iniciando classificacao, com ' +  str(decisoes_test.count()) + ' decisoes de teste'

    for decisao in decisoes_test:
        r = db.result.find_one({'acordaoId': decisao['acordaoId']})

        if r is None:
            print 'classificando...'
            result = cl.classify(decisao['decisao'].encode('utf-8'))
            db.result.insert({'acordaoId': decisao['acordaoId'], 'decisao': decisao['decisao'], 'classificacao': result})
        else:
            print 'ja classificado...'