#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import string

numberset = set('1234567890')


def ascitest(x):
    x = x.lower()
    for (i, key) in enumerate(x):
        if key in string.ascii_lowercase or key in numberset:
            return x[i:]


def dfsTree(currentpath, prefix):
    f = [x for x in os.listdir(currentpath) if x[0] != '.']
    f = sorted(f, key=ascitest)
    dirN, fileN = 0, 0
    for i, fname in enumerate(f):
        if i < len(f) - 1:
            curPrefix, subdirPrefix = "|-- ", "|   "
        else:
            curPrefix, subdirPrefix = "`-- ", "    "
        print(prefix + curPrefix + fname)
        if os.path.isfile(os.path.join(currentpath, fname)):
            fileN += 1
        else:
            dirN += 1
            tdirN, tfileN = dfsTree(os.path.join(currentpath, fname), prefix + subdirPrefix)
            dirN, fileN = dirN + tdirN, fileN + tfileN
    return dirN, fileN


def tree(path):
    print(path)
    dirN, fileN = dfsTree(path, "")
    print()
    print(str(dirN) + (" directories, " if dirN != 1 else " directorie, ") + str(fileN) + (" files" if fileN != 1 else " files"))



if __name__ == '__main__':
		if len(sys.argv)> 1:
			path = sys.argv[1] 
		else:
			path = "."
		tree(path)
