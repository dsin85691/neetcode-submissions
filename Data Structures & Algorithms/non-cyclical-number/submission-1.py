class Solution:
    def isHappy(self, n: int) -> bool:
        
        non_cyclical = n 
        hash_map = set()

        while non_cyclical != 1: 
            new_num = self.sum_squares(non_cyclical) 

            if new_num in hash_map: 
                return False 
            hash_map.add(non_cyclical)
            non_cyclical = new_num
        return True 
        
    def sum_squares(self, num): 
        sum_digits_sq = 0 
        while num > 0:
            digit = num % 10 
            sum_digits_sq += digit ** 2 
            num = num // 10
        return sum_digits_sq