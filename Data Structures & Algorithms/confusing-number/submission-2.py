class Solution:
    def confusingNumber(self, n: int) -> bool:
        original_n = n
        rotated_n = 0
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        hash_set = set([2,3,4,5,7])
        if n == 0: return False
        while n > 0: 
            digit = n % 10 
            n = n // 10 
            if digit in hash_set:
                return False
            rotated_n = rotated_n * 10 + mapping[digit]
        return rotated_n != original_n