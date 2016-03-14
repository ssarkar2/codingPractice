#https://www.hackerrank.com/challenges/lonely-integer

#!/usr/bin/py
def lonelyinteger(a):
    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1
    for i in d:
        if d[i] == 1:
            answer = i
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
