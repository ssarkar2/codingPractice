class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([i.lower() for i in s if i.isalnum()])
        if len(s) == 0 or len(s) == 1:
            return True
        if len(s) == 2:
            return s[0].lower() == s[1].lower()
        left = 0
        right = len(s) - 1
        while (right-left > 1):
            if s[left] != s[right]:
                return False
            else:
                left+=1
                right-=1
        return s[left] == s[right]
