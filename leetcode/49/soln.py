class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def hist(word):
            hist = [0 for i in range(26)]
            base = ord('a')
            for w in word:
                hist[ord(w) - base] += 1
            return tuple(hist)
        
        result = {}
        for word in strs:
            histkey = hist(word)
            result[histkey] = result.get(histkey, []) + [word]
        return result.values()

