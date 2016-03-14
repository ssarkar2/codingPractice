#https://www.hackerrank.com/challenges/interchange-two-numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
M = int(raw_input())
a = (N,M)
b=(a[1],a[0])
print b[0]
print b[1]