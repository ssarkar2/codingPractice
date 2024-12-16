class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(1 + 8*n) - 1) / 2)
