#https://www.hackerrank.com/challenges/pangrams
import sys

def f(str):
    flag = [0]*26
    count = 0
    for i in str:
        if i != ' ':
            t = ord(i.lower()) - 97
            if flag[t] == 0:
                count += 1
                flag[t] = 1
                if count == 26:
                    print 'pangram'
                    return
            else:
                flag[t] = 1
    print 'not pangram'


f(raw_input())