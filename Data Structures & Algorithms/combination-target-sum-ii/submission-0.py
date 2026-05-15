class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates) 
        n=len(candidates) 
        res=[] 
        curr_comb=[]
        self.helper(0, 0, curr_comb, res, candidates, target, n)
        return res
    
    def helper(self, i, curr_sum, curr_comb, ucombs, candidates, target, n): 

        if curr_sum == target: 
            if curr_comb not in ucombs:
                ucombs.append(curr_comb.copy()) 
            return 
        elif curr_sum > target: 
            return 
        if i >= n: 
            return 

        curr_sum+=candidates[i] 
        curr_comb.append(candidates[i])
        self.helper(i + 1, curr_sum, curr_comb, ucombs, candidates, target, n)

        curr_sum-=candidates[i] 
        curr_comb.pop()
        while i < len(candidates) - 1 and candidates[i] == candidates[i+1]: 
            i+=1
        self.helper(i + 1, curr_sum, curr_comb, ucombs, candidates, target, n)
        
        