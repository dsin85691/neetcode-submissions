class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_check = {} 
        for num in nums: 
            if num not in dup_check: 
                dup_check[num] = 1 
            else: 
                return True 
        return False