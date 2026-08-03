class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = None
        # O(n) time complexity, O(1) space
        for i in range(1,n): 
            # Monotone inc
            if nums[i] > nums[i-1]: 
                if inc is not None and not inc: 
                    return False
                inc = True
            # Monotone dec 
            if nums[i] < nums[i-1]: 
                if inc is not None and inc: 
                    return False
                inc = False
        return True