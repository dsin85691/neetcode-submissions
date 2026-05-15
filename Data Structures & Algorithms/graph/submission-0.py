from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {} 

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph: 
            self.graph[src] = [] 
        if dst not in self.graph: 
            self.graph[dst] = [] 
        self.graph[src].append(dst) 

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph: 
            return False
        
        key = False
        for n in self.graph[src].copy(): 
            if n == dst: 
                self.graph[src].remove(n) 
                key = True
        return key

    def hasPath(self, src: int, dst: int) -> bool:

        visits = set() 
        queue = deque() 
        queue.append(src)

        while queue: 

            for i in range(len(queue)): 

                node = queue.popleft() 

                if node == dst: 
                    return True

                for n in self.graph[node]: 
                    if n not in visits: 
                        visits.add(n)
                        queue.append(n) 

        return False

