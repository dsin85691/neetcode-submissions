class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter() 
        for i in range(len(nums)): 
            counter[nums[i]]+=1 
        heap = [] 
        for key in counter.keys(): 
            heapq.heappush(heap, (-counter[key], key))
        return [heapq.heappop(heap)[1] for i in range(k)]