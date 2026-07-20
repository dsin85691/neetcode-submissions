class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {} 

        for i in range(n): 
            adj[i] = [] 
        
        for nodes, prob in zip(edges, succProb):
            src, dest = nodes 
            adj[src].append((dest, prob))
            adj[dest].append((src, prob)) # Undirected edge

        shortest = {} 
        maxHeap = [[-1, start_node]] # Want to start with a prob 1 from src


        while maxHeap: 

            succ_prob, node = heapq.heappop(maxHeap)

            if node in shortest: 
                continue 
            
            shortest[node] = succ_prob 

            for nei, nei_prob in adj[node]: 

                if nei not in shortest: 
                    heapq.heappush(maxHeap, (-1 * abs(succ_prob * nei_prob), nei)) 
        
        return -1 * shortest[end_node] if end_node in shortest else 0 # Prob is 0 if we cannot find it