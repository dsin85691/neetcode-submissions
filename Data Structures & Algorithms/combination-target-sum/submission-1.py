class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(idx, comb, total): 
            if total == target: 
                res.append(comb[:])
                return 
            
            if total > target or idx >= len(nums): 
                return 
            
            comb.append(nums[idx])
            dfs(idx, comb, total + nums[idx])
            comb.pop() 
            dfs(idx + 1, comb, total)
        dfs(0, [], 0)
        return res