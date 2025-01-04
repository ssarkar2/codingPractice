class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def gen_hist(word):
            hist = {}
            for k in word:
                hist[k] = hist.get(k,0) + 1
            return hist

        def find_all_anagrams(original, check):
            hist_window = gen_hist(original[:len(check)])    
            hist_check = gen_hist(check)
            result = []
            if hist_window == hist_check:
                result += [0]
            for i in range(1, len(original)-len(check)+1):
                curr_letter = original[i+len(check)-1]
                old_letter = original[i-1]
                hist_window[curr_letter] = hist_window.get(curr_letter,0)+1
                hist_window[old_letter] = hist_window[old_letter]-1
                if hist_window[old_letter] == 0:
                    hist_window.pop(old_letter)
                if hist_window == hist_check:
                    result += [i]
            return result
        return find_all_anagrams(s, p)
