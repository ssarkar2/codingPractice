#!/bin/python
#https://www.hackerrank.com/challenges/mini-max-sum/problem
import sys

def miniMaxSum(arr):
    sm = sum(arr)
    tmp = [sm - i for i in arr]
    return str(min(tmp)) + ' ' + str(max(tmp))


if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    print miniMaxSum(arr)
