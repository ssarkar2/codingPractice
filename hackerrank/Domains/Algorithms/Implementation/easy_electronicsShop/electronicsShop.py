#!/bin/python
#https://www.hackerrank.com/challenges/electronics-shop/problem
import sys

def getMoneySpent(keyboards, drives, s):
    spent = -1
    for k in keyboards:
        for d in drives:
            if spent<(k+d)<=s:
                spent = k+d
    return spent

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
