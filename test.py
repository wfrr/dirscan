#!/usr/bin/env python3

import pickle, os, sys, manage_db

def getkeys():
    db = pickle.load(open( "save.p", "rb" ))
    for k in db:
        #print(k, ' > ', db[k])
        print(k)
    print(db['date'])

def exclude_dir():
    home_dir = os.getenv('HOME')
    exclude = [str(home_dir + "/."), str(home_dir + "/Library")]
    for dirpath, dirname, filename in os.walk(home_dir):
        if (exclude[0] not in dirpath) and (exclude[1] not in dirpath):
            print(dirpath)

if __name__ == '__main__':
    #getkeys()
    for ar in sys.argv:
        if ar == 'compare':
            print('got!')
