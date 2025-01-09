class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroloc = [i for i in range(len(nums)) if nums[i] == 0]
        zeroloc = [-1] + zeroloc + [len(nums)]

        def prod(x):
            if len(x) == 0:
                return None
            p = 1
            for i in x:
                p *= i
            return p

        def helper(arr):
            #print('...', arr)
            # assert no elem of arr is 0
            negloc = [i for i in range(len(arr)) if arr[i] < 0]
            #print(negloc, '..')
            if len(negloc) %2 == 0:
                return prod(arr)
            else:

                # negloc is 3 or more
                '''
                [A n1 B n2 C n3 D]
                [A n1 B n2 C ]
                [B n2 C n3 D]
                '''
                first_sec = prod(arr[0:negloc[-1]])
                second_sec = prod(arr[negloc[0]+1:])
                #print('XXX', first_sec, second_sec)
                if first_sec is None and second_sec is not None:
                    return second_sec
                elif second_sec is None and first_sec is not None:
                    return first_sec
                elif first_sec is None and second_sec is None:
                    return arr[0] if len(arr) == 1 else 0
                else:
                    return first_sec if first_sec > second_sec else second_sec

        x = max([helper(nums[i+1:j]) for i,j in zip(zeroloc, zeroloc[1:])] + ([0] if len(zeroloc)>2 else []))
        #print(zeroloc, [helper(nums[i+1:j]) for i,j in zip(zeroloc, zeroloc[1:])])
        return x
        
