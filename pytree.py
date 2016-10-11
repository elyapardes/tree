#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os import listdir, sep, walk
from os.path import basename, isdir
import re

import string
import sys

def count_file(files, num_file):
    totalfile = []
    for f in files:
        if not f.startswith('.'):
            totalfile.append(f)
    nfile = len(totalfile)
    return nfile

def tree(dir, spacing, flaglast=False):
    files = []
    files = [files for files in listdir(dir) if not files.startswith('.')]
    allfiles = sorted(files, key=lambda x: x.lower())
    for i, filename in enumerate(allfiles):
        path = dir + sep + filename
        if (i == len(files) - 1):
            flaglast = True
            print(spacing + '└── ' + filename)
        else:
            flaglast = False
            print(spacing + '├── ' + filename)
        printDir(path, spacing, flaglast)
    spacing = spacing + '    '

    def printDir(path, spacing, flaglast):
    if isdir(path):
        if flaglast:
            spacing = spacing + '    '
            tree(path, spacing, flaglast=False)
        else:
            spacing = spacing + '│   '
            tree(path, spacing, flaglast=False)

def fileTrack(path):
    ndir = 0
    nfiles = 0
    for path, dirs, files in walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        ndir = ndir + len(dirs)
        nfile = count_file(files, nfiles)
        nfiles += nfile
    print("%s directories, %s files" % (ndir, nfiles))

# Code was written with the help of classmate, and using stackoverflow
    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        path = os.getcwd()
        no_files = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        no_files = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
