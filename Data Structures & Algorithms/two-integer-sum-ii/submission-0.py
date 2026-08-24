class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1 
        while L < R: 
            sum_val = numbers[L] + numbers[R] 
            if sum_val > target: 
                R-=1 
            elif sum_val < target: 
                L+=1 
            else: 
                return [L + 1,R + 1]
            