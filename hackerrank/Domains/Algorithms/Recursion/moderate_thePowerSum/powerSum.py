#!/bin/python
#https://www.hackerrank.com/challenges/the-power-sum/problem
import sys

def helper(X,N,lst):
    if len(lst)==0:
        return 0
    item = lst[0]
    diff = X-item**N
    tmp1 = 0
    if diff > 0:
        tmp1 = helper(diff, N, lst[1:])
    elif diff==0:
        tmp1 = 1
    tmp2 = helper(X, N, lst[1:])
    return tmp1+tmp2
    

def powerSum(X, N):
    # Complete this function
    max_int = int(X**(1.0/N)) #floor
    return helper(X, N, range(1,max_int+1))

if __name__ == "__main__":
    
    X = int(raw_input().strip())
    N = int(raw_input().strip())
    result = powerSum(X, N)
    print result
    '''
    print powerSum(100, 2)
    print powerSum(100, 3)
    print powerSum(10, 2)
    #print powerSum(28, 3)
    #print 'ddddddddddddd'
    #print helper(28,3,[2,3])
    print 'ddddddddddddd'
    #print helper(28,3,[1,3])
    print 'ddddddddddddd'
    #print helper(28,3,[2,1])
    '''