#!/usr/bin/env python
import os
import sys
 

def main():
    ARGS = sys.argv[1:]
    PATH = os.environ['PATH']
    PATH_NEW = []
 
    for arg in ARGS:
        for path in PATH.split(':'):
            if arg in path:
                continue
            PATH_NEW.append(path)   
 
    print("{0}".format(":".join(PATH_NEW)))


if __name__ in '__main__':
    main()
