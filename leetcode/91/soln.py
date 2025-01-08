class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def valid_2digit(num_str):
            assert len(num_str) == 2
            intnum = int(num_str)
            return (10 <= intnum) and (intnum <= 26)
        memo = {}
        def helper(idx):
            if idx in memo:
                return memo[idx]
            if idx == len(s)-1 and s[idx]!='0': # 1 letter left
                #print('base0')
                memo[idx] = 1
                return 1
            if idx == len(s): # no letters left
                #print('base1')
                memo[idx] = 0
                return 0

            x = 0
            first = s[idx]
            if idx <= len(s)-2:
                first2 = s[idx:idx+2]
            if first != '0':
                x += helper(idx+1)

            if idx <= len(s)-2 and valid_2digit(first2):
                if idx == len(s)-2:
                    #print("base3")
                    x += 1
                else:
                    x += helper(idx+2)
            #print(idx, x)
            memo[idx] = x
            return x


        return helper(0)

            
        
