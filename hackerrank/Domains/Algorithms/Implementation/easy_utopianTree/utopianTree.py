#https://www.hackerrank.com/challenges/utopian-tree
#!/bin/python

import sys

def f(x):
    num = 1;
    for i in range(0,x):
        if i%2 == 0:
            num *= 2
        else:
            num += 1
    return num


t = int(raw_input().strip())
inp = []
for a0 in xrange(t):
    n = int(raw_input().strip())
    inp.append(n)
for i in inp:
    print f(i)
