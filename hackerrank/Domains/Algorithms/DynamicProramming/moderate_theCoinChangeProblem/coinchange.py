#!/bin/python
#https://www.hackerrank.com/challenges/coin-change/problem
import sys
tbl = {}
def helper(n,c):
    #print n,c
    if n==0:
        return 1
    if len(c) == 0:
        return 0
    currcoin = c[0]
    currcoin_possibilities = n/currcoin
    sm = 0
    for num_curr_coin in range(currcoin_possibilities+1):
        key = tuple([n-num_curr_coin*currcoin] + c[1:])
        #tmp = table.get(key, helper(n-num_curr_coin*currcoin, c[1:])) #bad idea. non lazy
        if key in tbl:
            tmp = tbl[key]
        else:
            tmp = helper(n-num_curr_coin*currcoin, c[1:])
            tbl[key] = tmp
        sm += tmp
    #print sm, 'xxx'
    return sm
def getWays(n, c):
    global tbl 
    tbl = {}
    #coins = sorted(c)[::-1]
    return helper(n,c)

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print ways


#print getWays(4, [1,2,3])
#print getWays(10, [2, 5, 3, 6])
