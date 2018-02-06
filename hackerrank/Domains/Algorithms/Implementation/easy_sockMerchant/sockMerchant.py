#!/bin/python
#https://www.hackerrank.com/challenges/sock-merchant/problem
import sys

def sockMerchant(n, ar):
    d = {}
    for k in ar:
        d[k] = d.get(k,0)+1
    return sum([i/2 for i in d.values()])

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
