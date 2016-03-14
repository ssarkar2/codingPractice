#https://www.hackerrank.com/challenges/cipher
import sys, math

def solve(a,b):
    #solve for x: x xor a = b
    if a == '0':
        if b == '0':
            return '1'
        else:
            return '0'
    if a == '1':
        if b == '0':
            return '0'
        else:
            return '1'

#1110100110

def f(S, N, K):
    B = [-1]*N; B[0] = S[0]; prev = B[0]
    #print S[0],S
    for i in range(1,N):
        #B[i] = solve(prev, S[i])
        if i-K >= 0:
            rest = S[i-1] ^ B[i-(K)]
            B[i] = S[i] ^ rest
            #print i, rest, S[i], B[i]
        else:
            B[i] = S[i]^S[i-1]
        #print S[i], B
    print ''.join([str(i) for i in B])


t = raw_input().split(); N = int(t[0]); K = int(t[1])
#inp = list(raw_input())
inp = [int(i) for i in list(raw_input())]

f(inp, N, K)