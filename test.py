#!/usr/bin/env python3

import pickle, os, sys, manage_db



def getkeys():
    db = pickle.load(open( "save.p", "rb" ))
    for k in db:
        #print(k, ' > ', db[k])
        print(k)
    print(db['date'])

if __name__ == '__main__':
    getkeys()
