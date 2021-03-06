#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os import listdir, sep, walk
from os.path import basename, isdir
import re
import string
import sys

spaces = '    '
indir = '│   '
lastindir = '└── '
newdir = '├── '


def printDir(path, spacing, flaglast):
    if isdir(path):
        if flaglast:
            spacing = spacing + spaces
            tree(path, spacing, flaglast=False)
        else:
            spacing = spacing + indir
            tree(path, spacing, flaglast=False)


def tree(dir, spacing, flaglast=False):
    files = []
    files = [files for files in listdir(dir) if not files.startswith('.')]
    allfiles = sorted(files, key=lambda x: x.lower())
    for i, filename in enumerate(allfiles):
        path = dir + sep + filename
        if (i == len(files) - 1):
            flaglast = True
            print(spacing + lastindir + filename)
        else:
            flaglast = False
            print(spacing + newdir + filename)
        printDir(path, spacing, flaglast)
    spacing = spacing + spaces


def fileTrack(path):
    ndir = 0
    nfiles = 0
    for path, dirs, files in walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        ndir = ndir + len(dirs)
        num_file = count_file(files, nfiles)
        nfiles += num_file
    print("%s directories, %s files" % (ndir, nfiles))


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
        no_files = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        no_files = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
