__author__ = 'brito'

from pymongo import MongoClient
import re

if __name__ == '__main__':

    connection = MongoClient('localhost', 27017)
    db = connection['DJs']

    acordaos = db.preprocessed.find({"$and": [{"decisao": {"$not": re.compile("embargos")}},
                                              {"decisao": {"$not": re.compile("provimento")}},
                                              {"decisao": {"$not": re.compile("procedente")}},
                                              {"decisao": {"$not": re.compile("improcedente")}},
                                              {"decisao": {"$not": re.compile("habeas corpus")}},
                                              {"$or": [{"decisao": re.compile("indefer")},
                                                       {"decisao": re.compile("deneg")},
                                                       {"decisao": re.compile("desprovi")}]}]})

    size = acordaos.count()

    print 'Total ' + str(size)

    size_p = int(size * 0.2)

    print 'Total que ser inserido ' + str(size_p)

    for i in range(0, size_p):
        acordao = db.trained.find_one({"acordaoId": acordaos[i]['acordaoId']})

        if acordao is None:
            db.trained.insert({'acordaoId': acordaos[i]['acordaoId'],
                           'decisao': acordaos[i]['decisao'],
                           'classificao': 'neg'})
        else:
            print acordao['acordaoId'] + ' ja esta inserido'

