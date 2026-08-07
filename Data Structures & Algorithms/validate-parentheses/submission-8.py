class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        dict_values = { 
            ")": "(", 
            "]":"[", 
            "}":"{"
        }

        for char in s: 
            if char in "([{":
                stack.append(char) 
            else: 
                if stack:
                    if dict_values[char] == stack[-1]:
                        stack.pop() 
                    else:
                        return False
                else: 
                    return False

        return len(stack) == 0 


            