class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # swap so than m<n
        if m > n:
            t = m
            m = n
            n = t
        m = m-1
        n = n-1
        # now need to calculate: (m+n)! / (m!*n!)
        # or (n+1 * n+2 ... n+m) / m!
        prod = 1
        for i in range(n+1, n+m+1):
            prod *= i
        for i in range(1, m+1):
            prod /= i
        return int(prod)
