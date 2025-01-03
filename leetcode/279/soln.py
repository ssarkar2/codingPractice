import sys
import math
sys.setrecursionlimit(10000)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        
        def issq(x):
            y = int(round(math.sqrt(x)))
            return y*y == x
            
        def perfect_squares(n):
            '''
            f(i) is a func that says: smallest number of squares needed to construct i
            '''
            
            memo = {}

            def f(i):
                if i in memo:
                    return memo[i]
                #print(i)
                if issq(i): # also takes care of i==1
                    memo[i] = 1
                    return 1
                cnt = 1
                target = i
                collect_results = []
                while(target > 0):
                    target = i - cnt*cnt
                    if target < 0:
                        break
                    val = f(target)
                    collect_results += [val+1]
                    cnt += 1
                x = min(collect_results)
                memo[i] = x
                return x
            
            
            return f(n)
        return perfect_squares(n)
                
