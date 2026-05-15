class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comp_map = {} 

        for i in range(len(nums)): 
            print(comp_map)
            if target-nums[i] not in comp_map: 
                comp_map[nums[i]] = i
            else: 
                return [comp_map[target-nums[i]], i]