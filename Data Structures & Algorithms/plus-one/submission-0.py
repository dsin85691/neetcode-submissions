class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        r = len(digits) - 1 

        for r in range(r, -1, -1): 
            # Adds one in reverse
            new_val = digits[r] + 1

            # If the new value is less than 10, return
            if new_val < 10: 
                digits[r] += 1 
                return digits
            # Reduces back to 0 
            digits[r] = 0 
        
        # Make sure to insert 1 at the start
        digits.insert(0, 1)
        return digits