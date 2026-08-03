class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        count = 0  
        for num in arr:
            if num + 1 in seen: 
                count+=1 
        return count