class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [] 
        s = s.strip() # remove whitespace at ends 
        return len(s.split()[-1])
         