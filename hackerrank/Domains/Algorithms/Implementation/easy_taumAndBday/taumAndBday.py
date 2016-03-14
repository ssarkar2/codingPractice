#https://www.hackerrank.com/challenges/taum-and-bday
#!/bin/python

import sys

def f(b,w,x,y,z):
    return b * min(x, y+z) + w * min(y, x+z)


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print f(b,w,x,y,z)
