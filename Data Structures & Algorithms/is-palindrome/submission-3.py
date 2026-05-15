class Solution:
   def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        
        while L < R:
            # Move L to the next alphanumeric character
            while L < R and not s[L].isalnum():
                L += 1
            # Move R to the previous alphanumeric character
            while L < R and not s[R].isalnum():
                R -= 1
                
            # Compare characters
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True