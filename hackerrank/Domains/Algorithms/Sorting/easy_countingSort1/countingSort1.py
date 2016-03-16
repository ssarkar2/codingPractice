#https://www.hackerrank.com/challenges/countingsort1
def f(a,n):
    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1
    for i in range(n):
        print d.get(i,0),
        

n = int(raw_input())
arr = [int(i) for i in raw_input().split()]
f(arr,100)