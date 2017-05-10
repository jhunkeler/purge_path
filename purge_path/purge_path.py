#!/usr/bin/env python
from __future__ import print_function
import os
import sys


def purge(path, pattern):
    if not isinstance(path, list):
        path = path.split(':')

    path_new = ''
    for rec in path:
        if rec == pattern:
            # ignore pattern
            continue
        path_new += rec + ':'

    return path_new[:-1]


def main():
    args = sys.argv[1:]
    path_orig = os.environ['PATH']
    path_new = path_orig

    for arg in args:
        path_new = purge(path_new, arg)

    if path_new:
        print(path_new)
    else:
        print(path_orig)


if __name__ in '__main__':
    main()
