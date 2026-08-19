class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val, min_for_max = -float("inf"), float("inf")
        min_val, max_for_min = float("inf"), -float("inf")
        i_max, i_min = -1, -1 
        for i in range(len(arrays)): 
            if arrays[i][len(arrays[i])-1] > max_val:
                max_val = arrays[i][len(arrays[i])-1]
                i_max = i 
            if arrays[i][0] < min_val:
                min_val = arrays[i][0]
                i_min = i 
        for j in range(len(arrays)): 
            if i_max != j: 
                min_for_max = min(arrays[j][0], min_for_max)
            if i_min != j: 
                max_for_min = max(arrays[j][len(arrays[j])-1], max_for_min)
        return max(max_val - min_for_max, max_for_min - min_val)

