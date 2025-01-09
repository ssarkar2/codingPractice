class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_num = set([])
        for i in nums:
            if i in set_num:
                return True
            else:
                set_num.update([i])
        return False
