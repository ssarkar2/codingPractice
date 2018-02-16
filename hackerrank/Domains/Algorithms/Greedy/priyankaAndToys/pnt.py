#!/bin/python
#https://www.hackerrank.com/challenges/priyanka-and-toys/problem
import sys

def toys(w):
    # Complete this function
    wsort = sorted(w)
    bought = [0]*len(w)
    cnt = 0
    for idx,wt in enumerate(wsort):
        if bought[idx]==0:
            cnt+=1
            bought[idx]=1
            kk=0
            while(True):
                if idx+kk < len(w) and wsort[idx+kk]<= wt+4:
                    bought[idx+kk]=1
                    kk+=1
                else:
                    break
    return cnt

if __name__ == "__main__":
    n = int(raw_input().strip())
    w = map(int, raw_input().strip().split(' '))
    result = toys(w)
    print result
