class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def subsetDFS(nums, subset, res): 
            res.append(subset.copy())
            for i in range(len(nums)): 
                subset.append(nums[i])
                sub_nums = nums[i+1:]
                subsetDFS(sub_nums, subset, res)
                subset.pop() 
        subsetDFS(nums, [], res)
        return res 