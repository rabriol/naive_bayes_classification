from pymongo import MongoClient
import psycopg2

__author__ = 'brito'

# coding=utf-8

if __name__ == '__main__':
    connection = MongoClient('localhost', 27017)
    mongodb = connection['DJs']

    try:
        postgresql = psycopg2.connect("dbname='' user='' host='' password=''")
    except:
        print "Error when connecting to database postgresql"

    decisoes = mongodb.all.find()

