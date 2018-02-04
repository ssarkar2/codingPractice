#!/bin/python
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import sys

def birthdayCakeCandles(n, ar):
    mx = max(ar)
    return len([i for i in ar if i == mx])

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
