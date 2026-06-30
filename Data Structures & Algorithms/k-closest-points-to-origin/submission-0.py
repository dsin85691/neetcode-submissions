class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.euc_dist(point), point) for point in points]
        heapq.heapify(heap) # O(n) 
        
        # O(n)
        top_k = [] 
        for _ in range(k): 
            top_k.append(heapq.heappop(heap)[1]) # Pop k times 

        return top_k
    

    def euc_dist(self, point): 
        return math.sqrt(sum([point[i]**2 for i in range(len(point))])) 