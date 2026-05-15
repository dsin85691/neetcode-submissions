class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False 

        validate_paren = [] 
        pairs = { "(": ")", "{":"}", "[":"]"}

        for char in s: 
            if char in "([{": 
                validate_paren.append(char) 
            else: 
                if len(validate_paren) == 0: 
                    return False 

                lastElem = validate_paren.pop()

                if pairs[lastElem] != char: 
                    return False

        
        return len(validate_paren) == 0