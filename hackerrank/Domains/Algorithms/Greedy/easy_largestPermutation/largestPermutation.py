#!/bin/python
#https://www.hackerrank.com/challenges/largest-permutation/problem
import sys

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def largestPermutation(k, arr):
    # Complete this function
    idxdict = {dt:i for i,dt in enumerate(arr)}
    currmaxelem = len(arr)
    currloc = 0
    k = min(k,len(arr))
    #for _ in range(k):
    while(k>0 and currmaxelem>0):
        maxidx = idxdict[currmaxelem]
        if maxidx != currloc:
            arr[maxidx] = arr[currloc]
            arr[currloc] = currmaxelem
            idxdict[currmaxelem] = currloc
            idxdict[arr[maxidx]] = maxidx #maxidx is the before-swap location of max element, which now contains the other element after the swap
            k-=1
        
        currmaxelem -= 1
        currloc += 1
    return arr
        

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = largestPermutation(k, arr)
    print " ".join(map(str, result))


