#https://www.hackerrank.com/challenges/closest-numbers

def f(arr):
    b = sorted(arr)
    mindiff = float("inf")
    mindiffarr = [None]*(len(b)-1); c = 0;
    for i in range(0,len(b)-1):
        d = b[i+1] - b[i]
        if (mindiff >= d):
            mindiff = d
            mindiffarr[c] = (d, b[i], b[i+1])
            c += 1

    for i in range(c):
        if mindiffarr[i][0] == mindiff:
            print mindiffarr[i][1], mindiffarr[i][2],
            
        

n = int(raw_input())
f([int(i) for i in raw_input().split()])