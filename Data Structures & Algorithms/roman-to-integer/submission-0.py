class Solution:
    def romanToInt(self, s: str) -> int:
        # Write your code here
        # O(1) space 
        arab_to_roman = { 
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        res = 0 
        i = len(s) - 1
        # O(n) time complexity 
        while i >= 0: 
            roman_num = s[i] # Pop a roman numeral 
            if i >= 1 and arab_to_roman[s[i-1]] < arab_to_roman[roman_num]: 
                prev_num = arab_to_roman[s[i-1]]
                res -= prev_num
                i -= 1
            res += arab_to_roman[roman_num]
            i -= 1 
        return res
        
