class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # O(n), O(1) space
        candidate, vote = nums[0], 1
        for i in range(1, len(nums)): 
            if vote <= 0: 
                candidate = nums[i]
            if nums[i] == candidate:
                vote += 1
            else:
                vote -= 1 

        if nums.count(candidate) <= len(nums) // 2:
            return False

        L, R = 0, len(nums) - 1 
        while L <= R: 
            mid = (L + R) // 2 
            if nums[mid] == target: 
                return nums[mid] == candidate
            elif mid < target: 
                L = mid + 1 
            else: 
                R = mid - 1 
        return mid == candidate