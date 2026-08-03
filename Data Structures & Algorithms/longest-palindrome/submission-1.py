class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter() 
        has_odd = False
        len_max = 0
        for s_i in s: 
            freq[s_i]+=1
        for key in freq: 
            if freq[key] % 2 == 0: 
                len_max += freq[key] 
            else: 
                len_max += freq[key] - 1
                has_odd = True
        return len_max + 1 if has_odd else len_max