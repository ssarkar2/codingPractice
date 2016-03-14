#https://www.hackerrank.com/challenges/and-product
import sys, math

def digits(x):
    return int(math.ceil(math.log(x+0.1,2)))


def f(inp):
    if (digits(inp[0]) == digits(inp[1])):
        D = 2**digits(inp[1]-inp[0]) - 1
        print inp[0]&inp[1]&(0xFFFFFFFF^D)
    else:
        print 0

n = int(raw_input())
inp = []
for i in range(0,n):
    t = raw_input().split()
    inp.append([int(t[0]), int(t[1])])

for i in inp:
    f(i)