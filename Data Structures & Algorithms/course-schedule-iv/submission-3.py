class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
            isPrereq[crs][prereq] = True

        def dfs(crs, prereq):
            if isPrereq[crs][prereq] != -1:
                return isPrereq[crs][prereq] == 1

            for pre in adj[crs]:
                if pre == prereq or dfs(pre, prereq):
                    isPrereq[crs][prereq] = 1
                    return True

            isPrereq[crs][prereq] = 0
            return False

        res = []
        for u, v in queries:
            res.append(dfs(v, u))
        return res
