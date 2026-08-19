class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        res = 0
        n = len(arrays[0])
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1, len(arrays)):
            n = len(arrays[i])
            res = max(res, max(abs(arrays[i][n - 1] - min_val),
                               abs(max_val - arrays[i][0])))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][n - 1])
        return res