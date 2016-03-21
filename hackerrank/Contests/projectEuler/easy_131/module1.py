#https://projecteuler.net/problem=131

import math

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def f(a):
    #find all numbers below a such that cube + prime = cube  (n and n+p must be primes). alsp they must be consecutive

    #generate all cubes:
    largest = int(math.ceil(a**(1/3.0)))
    cubes = [i**3 for i in range(1,largest+1)]

    ans = []
    for i in range(len(cubes)-1):
            t = cubes[i+1] - cubes[i]
            if is_prime(t) == True:
                ans.append((t, cubes[i]))
    return ans



print f(100)
#print f(1000000)