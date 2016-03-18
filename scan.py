#!/usr/bin/env python3

import os, os.path, sys, pickle, manage_db

def scanhomedir():
    user = os.getlogin()
    home_dir = os.getenv('HOME')
    all_dirpaths = []

    for dirpath, dirname, filename in os.walk(home_dir):
            if filename:
                for f in filename:
                    all_dirpaths.append(dirpath + "/" + f)
    return all_dirpaths

def check_updates():
    all_dirpaths = scanhomedir()
    old_dirpaths = manage_db.load_db()
    print('\nREMOVED\n')
    for r in list(set(old_dirpaths['dirpaths'])-set(all_dirpaths)):
        print(r)
    print('\n' + '#' * 70)
    print('\nADDED\n')
    total_size = 0
    for a in list(set(all_dirpaths)-set(old_dirpaths['dirpaths'])):
        size = os.path.getsize(a) / 1024
        total_size += size
        print(a + '\n --> ' + str(round(size)) + 'Kb')
    print('\n total added: ' +  str(round(total_size)) + 'Kb')
    return all_dirpaths

def save_new(all_dirpaths):
    manage_db.update_db(all_dirpaths)
    print('\nDATA BASE UPDATED!\n')


if __name__ == '__main__':
    all_dirpaths = check_updates()
    save_new(all_dirpaths)
