#!/bin/python

import sys

def equal(arr):
    # Complete this function
    #for smallest in range(min(arr),-1,-1):
    mnmoves = -1
    #the '-4' is a bit hacky. passes test 15
    for smallest in range(-4,min(arr)+1):
        nummoves = 0
        for k in arr:
            if k != smallest:
                move5 = (k-smallest)/5
                move2 = (k-smallest-move5*5)/2
                move1 = (k-smallest-move5*5-move2*2)
                nummoves += (move5+move2+move1)
                if mnmoves >= 0:
                    if nummoves > mnmoves:
                        break
        if mnmoves > nummoves or mnmoves < 0:
            mnmoves = nummoves
        print mnmoves
    return mnmoves
    

if __name__ == "__main__":
    
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = equal(arr)
        print result
    '''
    print equal([2,2,3,7])
    #print equal([2, 5, 5, 5, 5, 5]) #expected 6, got 10
    '''
