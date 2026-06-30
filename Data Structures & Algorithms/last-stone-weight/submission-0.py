import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [] 

        # O(n log n) 
        for stone in stones: 
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1: 
            # two largest
            largest, sec_largest = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap) 

            # Adding back in largest
            if largest > sec_largest: 
                new_stone = largest - sec_largest # y - x 
                heapq.heappush(heap, -1* new_stone)
        
        return -1 * heap[0] if len(heap) == 1 else 0