class HitCounter:

    def __init__(self):
        # Counts the expiration of each hit O(log n) 
        self.heap = [] 
        # Length of the heap (number of hits) 
        self.num_heap = 0 


    def hit(self, timestamp: int) -> None:
        # Add new elem
        self.num_heap += 1 
        # Push to the heap
        # Add 300 seconds for the exp date
        heapq.heappush(self.heap, ("h", timestamp + 300))

    def getHits(self, timestamp: int) -> int:
        # Remove all hits such that hit exp date < timestamp 
        # Remove all that expired 
        while self.num_heap > 0 and self.heap[0][1] <= timestamp: 
            # Pop from the heap those elems such that timestamp > self.heap[0] (exp date)
            heapq.heappop(self.heap)
            # Remove one elem at a time
            self.num_heap-=1
        print(self.heap)
        return self.num_heap # Remaining number of hits within the past 300 secs


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
