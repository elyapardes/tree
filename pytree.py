#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os import listdir, sep, walk
from os.path import basename, isdir
import re
import string
import sys

def printdirectory(path, spacing, flaglast):
    if isdir(path):
        if flaglast:
            spacing = spacing + '    '
            tree(path, spacing, flaglast=False)
        else:
            spacing = spacing + '│   '
            tree(path, spacing, flaglast=False)


def tree(dir, spacing, flaglast=False):
    files = []
# Reference: http://stackoverflow.com/questions/7099290/how-to-ignore-hidden-files-using-os-listdir
    files = [files for files in listdir(dir) if not files.startswith('.')]
# Reference: http://stackoverflow.com/questions/13589560/how-to-sort-list-of-string-without-considering-special-characters-and-with-case
# allfiles = sorted(files, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
    allfiles = sorted(files, key=lambda x: x.lower())
    for i, filename in enumerate(allfiles):
        path = dir + sep + filename
        if (i == len(files) - 1):
            flaglast = True
            print(spacing + '└── ' + filename)
        else:
            flaglast = False
            print(spacing + '├── ' + filename)
        printdirectory(path, spacing, flaglast)
    spacing = spacing + '    '


# function to track number of directories and files in given path
def fileTrack(path):
    ndir = 0
    nfiles = 0
    for path, dirs, files in walk(path):
        # Reference: http://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        ndir = ndir + len(dirs)
        nfile = count_file(files, nfiles)
        nfiles += nfile
    print("%s directories, %s files" % (ndir, nfiles))


# function to fix complexity issue by codeclimate
def count_file(files, nfile):
    totalfile = []
    for f in files:
        if not f.startswith('.'):
            totalfile.append(f)
    nfile = len(totalfile)
    return nfile


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        path = os.getcwd()
        nofiles = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        nofiles = tree(path, '', flaglast=False)
        print('')
        fileTrack(path)
    else:
        print('Please enter with only one path.')
