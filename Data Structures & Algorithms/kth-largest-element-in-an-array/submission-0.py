class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [] 
        # Maintains a heap with k elems at most 
        # O (n log k) 
        # space: O(k) since at most k elems
        for n in nums: 
            heapq.heappush(heap, n)
            if len(heap) > k: 
                heapq.heappop(heap) # Remove the smallest elem where len(heap) > k 
        
        # Total time complex: O(n log k), space: O(k) 
        return heap[0] 