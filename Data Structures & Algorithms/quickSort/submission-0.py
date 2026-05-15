# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s, e = 0, len(pairs)-1
        return self.quickSortHelper(pairs, s, e)

    def quickSortHelper(self, pairs, s, e): 
        if e - s + 1 <= 1: 
            return pairs

        pivot = pairs[e] 
        left = s 

        for i in range(s, e): 
            if pairs[i].key < pivot.key: 
                tmp = pairs[left] 
                pairs[left] = pairs[i]
                pairs[i] = tmp 
                left += 1 
    
        pairs[e] = pairs[left] 
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left - 1)
        
        self.quickSortHelper(pairs, left + 1, e) 

        return pairs
            