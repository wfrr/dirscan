#!/usr/bin/env python3

import pickle, scan, datetime, time

def create_db():
    print('creating...')
    db = { 'dirpaths': scan.scanhomedir(), 'date': str(datetime.datetime.now())}
    pickle.dump(db, open('save.p', 'wb'))

def load_db():
    db = pickle.load(open( "save.p", "rb" ))
    return db

def update_db(all_dirpaths):
    db = load_db()
    db['dirpaths'] = all_dirpaths
    db['date'] = str(datetime.datetime.now())
    pickle.dump(db, open('save.p', 'wb'))

if __name__ == '__main__':
    create_db()
