#https://www.hackerrank.com/challenges/cut-the-sticks
#!/bin/python

import sys

def f(a):
    while(1):
        print len(a)
        m = min(a)
        a = [i-m for i in a if i > m]
        if a == []:
            break
        
        
    

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
f(arr)
