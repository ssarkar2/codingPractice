#https://www.hackerrank.com/challenges/sherlock-and-squares
import math

def f(arr):
    print int(math.floor(math.sqrt(arr[1])) - math.ceil(math.sqrt(arr[0]))) + 1

n = int(raw_input())
for i in range(n):
    f([int(i) for i in raw_input().split()])