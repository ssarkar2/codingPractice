#https://www.hackerrank.com/challenges/python-print
from __future__ import print_function
import sys
N = int(raw_input())
for i in range(1,N+1):
    print(i, sep='', end='', file=sys.stdout)
