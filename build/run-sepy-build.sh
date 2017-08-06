#!/usr/bin/env python36

import sys
import subprocess

def main():
    print('Run build in Python!')
    subprocess.check_call(['/usr/bin/python36', 'bootstrap.py'])
    return 0

if __name__ == '__main__':
    result = main()
    sys.exit(result)
