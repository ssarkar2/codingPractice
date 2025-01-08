class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        def flip(bins):
            return [1 if i==0 else 0 for i in bins]


        def twos_comp(bin_repr):
            #print('.x', bin_repr)
            bin_repr = flip(bin_repr)
            #print('..x', bin_repr)
            bin_repr = add_bins(bin_repr, [1] + [0]*11 )
            #print('..xxx', bin_repr)
            return bin_repr
        def convert_to_bin(n):
            bin_repr = [0]*12
            idx = 0
            val = abs(n)
            while(True):
                if val%2 == 1:
                    bin_repr[idx] = 1
                idx += 1
                val = val//2
                if val == 0:
                    break
            #print('..', bin_repr)
            if n < 0:
                bin_repr = twos_comp(bin_repr)
            return bin_repr

        def xor(x, y):
            return (x==0 and y==1) or (x==1 and y==0)
        
        def convertback(binrep):
            isneg = binrep[-1] == 1
            if isneg:
                binrep = twos_comp(binrep)
            sum = 0
            for i in range(len(binrep)):
                sum += binrep[i] * (2**i)
            return sum * [1,-1][isneg]



        def add_bins(b0, b1):
            carry = 0
            res = []
            for i, j in zip(b0, b1):
                curr_bit = [0,1][(not xor(i, j)) if carry==1 else xor(i, j)]
                carry = (i==1 and j==1) or (carry==1 and xor(i,j))
                res += [curr_bit]
            return res

        abin = convert_to_bin(a)
        bbin = convert_to_bin(b)
        return convertback(add_bins(abin, bbin))
