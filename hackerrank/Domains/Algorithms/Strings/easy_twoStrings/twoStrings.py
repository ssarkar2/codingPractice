#https://www.hackerrank.com/challenges/two-strings

def f(s1,s2):
    if len(set(s1).intersection(set(s2))) == 0:
        print 'NO'
    else:
        print 'YES'


n = int(raw_input())
for i in range(n):
    s1 = raw_input(); s2 = raw_input();
    f(s1,s2)

