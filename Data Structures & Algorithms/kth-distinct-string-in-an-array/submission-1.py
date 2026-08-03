class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct, seen = {}, set() 
        # Ensure we get distinct strings
        for i in range(len(arr)): 
            if arr[i] not in seen:
                distinct[arr[i]] = i
                seen.add(arr[i])
            else: 
                if arr[i] in distinct:
                    del distinct[arr[i]]
        distinct_idx = sorted(distinct.values())
        return arr[distinct_idx[k-1]] if k <= len(distinct_idx) else ""
        
        