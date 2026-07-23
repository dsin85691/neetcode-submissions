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
        elif self.rank[p2] > self.rank[p1]: 
            self.par[p1] = p2 
        else: 
            self.par[p1] = p2 
            self.rank[p2] += 1 
        return True 


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap  = [] 
        mst = [] 

        # Construct a union find set of all points
        union_find = UnionFind(n) 

        # O(n^2 log n)
        for i in range(n): 
            for j in range(i, n): 
                manhat_dist = self.manhat_dist(points[i], points[j])
                edge = (manhat_dist, i, j)
                heapq.heappush(minHeap, edge)
                
        while len(mst) < n - 1: 
            cost, pi, pj = heapq.heappop(minHeap) 

            # If we are not able to connect the two components, continue
            if not union_find.union(pi, pj): 
                continue

            mst.append(cost) 
        return sum(mst)


    def manhat_dist(self, x, y): 
        return abs(x[0] - y[0]) + abs(x[1] - y[1])