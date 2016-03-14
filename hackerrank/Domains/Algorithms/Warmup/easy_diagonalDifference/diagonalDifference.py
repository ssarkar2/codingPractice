#https://www.hackerrank.com/challenges/diagonal-difference
#!/bin/python

import sys

def f(a, n):
    return abs(sum([a[i][n-i-1] for i in range(n)]) - sum([a[i][i] for i in range(n)]))

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

print f(a, n)
