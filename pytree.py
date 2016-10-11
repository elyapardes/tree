#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import sys
import os
import re
from os import listdir, sep, walk
from os.path import basename, isdir


def printDir(path, padding, isLast):
    if isdir(path):
        if isLast:
            padding = padding + '    '
            tree(path, padding, isLast=False)
        else:
            padding = padding + '│   '
            tree(path, padding, isLast=False)


def tree(dir, padding, isLast=False):
    files = []
    files = [files for files in listdir(dir) if not files.startswith('.')]
    allfiles = sorted(files, key=lambda x: x.lower())
    for i, filename in enumerate(allfiles):
        path = dir + sep + filename
        if (i == len(files) - 1):
            isLast = True
            print(padding + '└── ' + filename)
        else:
            isLast = False
            print(padding + '├── ' + filename)
        printDir(path, padding, isLast)
    padding = padding + '    '


def fileTrack(path):
    num_dir = 0
    num_files = 0
    for path, dirs, files in walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        num_dir = num_dir + len(dirs)
        num_file = count_file(files, num_files)
        num_files += num_file
    print("%s directories, %s files" % (num_dir, num_files))

def count_file(files, num_file):
    total_file = []
    for f in files:
        if not f.startswith('.'):
            total_file.append(f)
    num_file = len(total_file)
    return num_file

# Code written with the help of classmates

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        path = os.getcwd()
        no_files = tree(path, '', isLast=False)
        print('')
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        no_files = tree(path, '', isLast=False)
        print('')
        fileTrack(path)
    else:
        print('Please enter with only one path.')
