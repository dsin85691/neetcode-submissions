class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while r < len(nums): 
            if nums[l] == 0:
                if abs(nums[l]) < abs(nums[r]): 
                    tmp = nums[r] 
                    nums[r] = nums[l]
                    nums[l] = tmp 
                    # Swap 
                    l += 1 # Move l pointer
            else: 
                l += 1 # Move 1 pointer (skip over it)
            r += 1 # Move upwards to maintain order