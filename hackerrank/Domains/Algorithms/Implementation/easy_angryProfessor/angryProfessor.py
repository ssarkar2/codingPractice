#https://www.hackerrank.com/challenges/angry-professor
#!/bin/python

import sys

def f(a,k):
    c=0
    for i in a:
        if i <= 0:
            c+=1
        if c >= k:
            print 'NO'; return
    print 'YES'


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    f(a,k)
