class UnionFind: 


    def __init__(self, n): 

        self.par = {} 
        self.rank = {} 

        for i in range(n): 
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
        elif self.rank[p1] < self.rank[p2]: 
            self.par[p1] = p2 
        else: 
            self.par[p1] = p2 
            self.rank[p2] += 1 
        return True 

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = [] 

        for n1, n2, weight in edges: 
            heapq.heappush(minHeap, [weight, n1, n2])

        unionFind = UnionFind(n) 
        mst = [] 

        while len(mst) < n - 1: 
            if len(minHeap) == 0: 
                return -1

            weight, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2): 
                continue 
            mst.append(weight)
        
        return sum(mst)