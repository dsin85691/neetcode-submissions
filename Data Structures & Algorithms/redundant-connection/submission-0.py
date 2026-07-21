class UnionFind: 

    def __init__(self, n): 
        self.par = {} 
        self.rank = {} 

        for i in range(1, n + 1): 
            self.par[i] = i 
            self.rank[i] = 0 
    
    def find(self, x): 

        if x != self.par[x]: 
            self.par[x] = self.find(self.par[x])
        return self.par[x] 

    def union(self, x, y): 

        p1, p2 = self.find(x), self.find(y) 

        if p1 == p2: 
            return False 
        
        if self.rank[p1] > self.rank[p2]: 
            self.par[p2] = p1 
        elif self.rank[p2] > self.rank[p1]: 
            self.par[p1] = p2 
        else: 
            self.par[p1] = p2
            self.rank[p2] += 1 
        return True 


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # By problem statement
        n = len(edges)
        # O(V + E*ack(V))  
        union_find = UnionFind(n)
        last_edge = None
        # O(E)
        for i, edge in enumerate(edges): 
            src, dest = edge
            if not union_find.union(src, dest): 
                last_edge = [src,dest] 
        return last_edge
            


