#https://www.hackerrank.com/challenges/alternating-characters

def f(inp):
    l = len(inp)
    c = 0
    prevchar = inp[0]
    for i in range(1,l):
        if prevchar == inp[i]:
            c += 1
        else:
            prevchar = inp[i]
    print c


num = int(raw_input())
for i in range(num):
    f(raw_input())


