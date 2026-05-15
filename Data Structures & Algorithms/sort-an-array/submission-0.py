class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: 
            return nums 
        midpoint = len(nums) // 2 
        print(midpoint)
        left_half = self.sortArray(nums[:midpoint])
        right_half = self.sortArray(nums[midpoint:]) 

        return self.merge(left_half, right_half) 

    def merge(self, left, right): 

        result = [] 
        i, j = 0, 0 

        while i < len(left) and j < len(right): 

            if left[i] < right[j]: 
                result.append(left[i])
                i+=1
            else: 
                result.append(right[j]) 
                j+=1 
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
            