class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1: 
            return intervals
        sort_ints = sorted(intervals)
        n = len(intervals)
        res = [sort_ints[0]]  
        target = None
        for i in range(1, n):  
            target = res[-1] 

            # Intersection between intervals
            if sort_ints[i][0] <= target[1]: 
                res.pop() # Pop from the res for the intersection
                res.append([min(target[0], sort_ints[i][0]), 
                            max(target[1], sort_ints[i][1])]) # Add int
            else: 
                res.append(sort_ints[i])
        return res
            