#!/bin/python
#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
import sys

def divisibleSumPairs(n, k, ar):
    sm = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j])%k == 0:
                sm += 1
    return sm

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
