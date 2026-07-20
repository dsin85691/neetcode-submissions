class UnionFind:
    
    def __init__(self, n: int):
        self.par = {} 
        self.rank = {} 
        self.num_components = n

        for i in range(n): 
            self.par[i] = i 
            self.rank[i] = 0 

    def find(self, x: int) -> int:
        if x != self.par[x]: 
            self.par[x] = self.find(self.par[x])
        return self.par[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y) 
        return p1 == p2

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y) 
        if p1 == p2: 
            return False 
        
        if self.rank[p1] > self.rank[p2]: 
            self.par[p2] = x 
        elif self.rank[p1] < self.rank[p2]: 
            self.par[p1] = p2 
        else: 
            self.par[p1] = p2 
            self.rank[p2] += 1
        self.num_components -= 1 # Reduce the num of components by 1 
        return True 

    def getNumComponents(self) -> int:
        return self.num_components
