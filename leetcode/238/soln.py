class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        num_zeros = 0
        for i in nums:
            if i==0:
                num_zeros += 1
            else:
                prod *= i
        zeros_found = num_zeros > 0
        for i in range(len(nums)):
            if num_zeros >= 2:
                nums[i] = 0
            else:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    if zeros_found:
                        nums[i] = 0
                    else:
                        nums[i] = prod / nums[i]
        return nums
