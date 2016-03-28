#!/usr/bin/env python3

import os, os.path, sys, pickle, manage_db

pro = False
nosave = False
hidden = False

def check_mods():
    if ('pro' in sys.argv) and ('hidden' in sys.argv):
        print('Choose "pro" OR "hidden"')
        exit()
    for ar in sys.argv:
        ar = str.lower(str(ar))
        if ar == 'pro':
            pro = True
        elif ar == 'nosave':
            nosave = True
        elif ar == 'hidden':
            hidden = True

def scanhomedir():
    user = os.getlogin()
    home_dir = os.getenv('HOME')
    all_dirpaths = []
    if pro:
        all_dirpaths = pro_scan(home_dir, all_dirpaths)
    elif hidden:
        all_dirpaths = scan_with_hidden(home_dir, all_dirpaths)
    else:
        all_dirpaths = usual_scan(home_dir, all_dirpaths)
    return all_dirpaths

def pro_scan(home_dir, all_dirpaths):
    for dirpath, dirname, filename in os.walk(home_dir):
            if filename:
                for f in filename:
                    all_dirpaths.append(dirpath + '/' + f)
    return all_dirpaths

def usual_scan(home_dir, all_dirpaths):
    exclude = [str('/.'), str(home_dir + '/Library')]
    for dirpath, dirname, filename in os.walk(home_dir):
        if (exclude[0] not in dirpath) and (exclude[1] not in dirpath):
            if filename:
                for f in filename:
                    all_dirpaths.append(dirpath + "/" + f)
    return all_dirpaths

def scan_with_hidden(home_dir, all_dirpaths):
    exclude = str(home_dir + '/Library')
    for dirpath, dirname, filename in os.walk(home_dir):
        if exclude not in dirpath:
            if filename:
                for f in filename:
                    all_dirpaths.append(dirpath + "/" + f)
    return all_dirpaths

def check_updates():
    old_dirpaths = manage_db.load_db()
    if old_dirpaths:
        all_dirpaths = scanhomedir()
        print('\nREMOVED\n')
        for r in list(set(old_dirpaths['dirpaths'])-set(all_dirpaths)):
            print(r)
        print('\n' + '#' * 70)
        print('\nADDED\n')
        total_size = size = 0
        for a in list(set(all_dirpaths)-set(old_dirpaths['dirpaths'])):
            try:
                size = os.path.getsize(a) / 1024
            except FileNotFoundError:
                size = 0
            total_size += size
            print(a + '\n --> ' + str(round(size)) + 'Kb')
        print('\ntotal added: ' +  str(round(total_size)) + 'Kb\n')
        return all_dirpaths
    else:
        print('exiting...')
        exit()

def save_new(all_dirpaths):
    manage_db.update_db(all_dirpaths)
    print('\nDATA BASE UPDATED!\n')


if __name__ == '__main__':
    check_mods()
    all_dirpaths = check_updates()
    if nosave:
        save_new(all_dirpaths)
