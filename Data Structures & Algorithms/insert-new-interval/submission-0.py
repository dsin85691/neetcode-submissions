class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] 
        target_start, target_end = newInterval
        inserted = False
        for start, end in intervals: 
            if end < target_start:
                res.append([start, end])
            elif start > target_end:
                if not inserted:
                    res.append([target_start, target_end])
                    inserted = True
                res.append([start, end])
            else:
                target_start = min(target_start, start)
                target_end = max(target_end, end)
        if not inserted:
            res.append([target_start, target_end])
        return res