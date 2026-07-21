class UnionFind: 

    def __init__(self, n): 

        self.par = {} 
        self.rank = {} 

        for i in range(n): 
            self.par[i]  = i 
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Graph Theory class Tree has n-1 edges
        if len(edges) != n-1: 
            return False 

        union_find = UnionFind(n) 
        n_comps = n 
        
        for edge in edges: 
            src, dest = edge 
            if union_find.union(src, dest): 
                n_comps -= 1 

        return n_comps == 1 


