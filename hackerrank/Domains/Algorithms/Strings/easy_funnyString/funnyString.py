#https://www.hackerrank.com/challenges/funny-string


def f(inp):
    ls = list(inp)
    N = len(ls)
    revls = [ls[N-i-1] for i in range(N)]
    for j in range(1,N):
        if abs(ord(ls[j])-ord(ls[j-1])) != abs(ord(revls[j])-ord(revls[j-1])):
            print 'Not Funny'
            return
    print 'Funny'


num = int(raw_input())
for i in range(num):
    f(raw_input())
    