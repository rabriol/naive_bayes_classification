__author__ = 'brito'

from pymongo import MongoClient

if __name__ == '__main__':

    connection = MongoClient('localhost', 27017)
    db = connection['DJs']
    preprocessed = db.preprocessed.find({})

    count = 0
    for i in preprocessed:
        acordao = db.trained.find_one({"acordaoId": i["acordaoId"]})
        if acordao is None:
            db.test.insert({"acordaoId": i["acordaoId"], "decisao": i["decisao"]})
        else:
            count += 1

    print 'Total de registro ignorados' + str(count)