class UnionFind: 

    def __init__(self, n): 
        self.par = {} 
        self.rank = {} 
        self.num_components = n 

        for i in range(n): 
            self.par[i] = i 
            self.rank[i] = 0
    
    def find(self, x): 
        if x != self.par[x]: 
            self.par[x] = self.find(self.par[x])
        return self.par[x] # Return root of the nodes

    def union(self, x, y): 
        p1, p2 = self.find(x), self.find(y) 
        if p1 == p2: 
            return False 
        
        if self.rank[p1] > self.rank[p2]: 
            self.par[p2] = p1 
        elif self.rank[p1] < self.rank[p2]: 
            self.par[p1] = p2 
        else: 
            self.par[p1] = p2 
            self.rank[p1] += 1 
        self.num_components -= 1 
        return True 


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Creates a discrete set with n nodes
        union_find = UnionFind(n) 

        num_comps = n 

        # O(E)
        for src, dest in edges: 
            if union_find.union(src, dest): 
                num_comps -= 1 # Reduce the num of comps by 1 
        return num_comps


        





