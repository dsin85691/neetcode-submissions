class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {} 

        for i in range(1, n + 1): 
            adj[i] = [] 

        for ui, vi, ti in times: 
            adj[ui].append([vi, ti])

        shortest = {} 
        minHeap = [[0, k]]
        while minHeap: 
            ti, ni = heapq.heappop(minHeap) 
            if ni in shortest: 
                continue
            shortest[ni] = ti 
            for nei_ni, nei_ti in adj[ni]: 
                if nei_ni not in shortest: 
                    heapq.heappush(minHeap, [ti + nei_ti, nei_ni])

        min_time = 0
        for i in range(1, n + 1): 
            if i not in shortest: 
                return -1
            min_time = max(shortest[i], min_time)
        return min_time