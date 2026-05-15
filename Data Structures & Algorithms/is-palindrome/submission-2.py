class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1 
        
        s = s.lower() 

        while L <= R: 
            
            if s[L].isalnum() and s[R].isalnum(): 
                if s[L] != s[R]: 
                    return False 
                L+=1
                R-=1
            elif s[L].isalnum(): 
                R-=1 
            elif s[R].isalnum(): 
                L+=1 
            else: 
                L+=1
                R-=1

        return True