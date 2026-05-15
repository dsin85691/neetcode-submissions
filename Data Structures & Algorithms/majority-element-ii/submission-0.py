class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        threshold = len(nums) // 3 
        list_majority = [] 
        i = 0
        while i < len(nums):
            count = 0
            j = i 
            while j < len(nums) and nums[j] == nums[i]: 
                count+=1
                j+=1
            if count > threshold: 
                list_majority.append(nums[i])
            i = j
        return list_majority