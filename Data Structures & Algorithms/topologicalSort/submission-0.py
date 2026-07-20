class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visit = set() # 0: unvisited, 1: visiting, 2: visited
        state = [0] * n
        for i in range(n):
            if not self.dfs(i, adj, state, topSort):
                return []
        topSort.reverse()
        return topSort

    def dfs(self, src, adj, state, topSort): 
        if state[src] == 1: 
            return False
        if state[src] == 2:
            return True
        
        state[src] = 1
        for neighbor in adj[src]: 
            if not self.dfs(neighbor, adj, state, topSort):
                return False
        state[src] = 2
        topSort.append(src)
        return True