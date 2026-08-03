class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter()
        odd_num = 0 
        for s_i in s: 
            counter[s_i]+=1 
        for key in counter:
            if counter[key] % 2 == 1: 
                odd_num+=1 
            
        return odd_num <= 1