class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        '''
        f(i,j) ... min num coins to make up "j" using first "i" coins

        f(i,j):
        f(i,j-c[i]).. min num of coins to make up j-c[i] using "i" coins
        f(i-1,j) ... min num of coins to make up "j" using "i-1" coins

        f(i,j) = min (f(i-1, j), 1+f(i,j-c[i]))
        '''
        f = [[None for __ in range(len(coins))] for _ in range(amount+1)]

        for i in range(amount+1):
            f[i][0] = i//coins[0] if i % coins[0] == 0 else -1
        for i in range(len(coins)):
            f[0][i] = 0
        for max_amount in range(1, amount+1):
            for num_coins_used in range(1, len(coins)):
                if num_coins_used-1 >= 0:
                    x = f[max_amount][num_coins_used-1]
                else:
                    x = -1
                if max_amount - coins[num_coins_used] >= 0:
                    y = f[max_amount - coins[num_coins_used]][num_coins_used]
                else:
                    y = -1

                if x > -1 and y > -1:
                    f[max_amount][num_coins_used] = min(x, y+1)
                elif x > -1:
                    f[max_amount][num_coins_used] = x
                elif y > -1:
                    f[max_amount][num_coins_used] = y+1
                else:
                    f[max_amount][num_coins_used] = -1
        x = [i for i in f[amount] if i >= 0]
        return -1 if len(x) == 0 else min(x)

        
