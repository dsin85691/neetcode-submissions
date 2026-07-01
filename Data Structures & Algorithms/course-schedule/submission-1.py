class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = {} 
        for i in range(numCourses): 
            adj[i] = [] 
        for src, dst in prerequisites: 
            adj[src].append(dst) 
        
        visit = set() 
        path = set() # list of nodes in the path 
        for i in range(numCourses): 
            if not self.dfs(i, adj, visit, path): 
                return False
        return  True

    def dfs(self, src, adj, visit, path): 
        # if we find the src node again in the node we return 
        if src in path: 
            return False
        if src in visit: 
            return True 

        visit.add(src) # Add to the visit set
        path.add(src) # Add it to the path

        all_paths = True 
        for neighbor in adj[src]: 
            all_paths = all_paths & self.dfs(neighbor, adj, visit, path)
        path.remove(src) # Remove the src node from the path (post-order)
        return all_paths 
        