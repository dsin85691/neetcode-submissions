class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = {} 

        for i in range(numCourses): 
            prereq[i] = [] 
        for pre_course, course in prerequisites: 
            prereq[course].append(pre_course) 
        
        answer = [] # Answer array
        for course_value, course_key in queries: 
            visit = set() 
            ans = self.dfs(course_key, course_value, prereq, visit)
            answer.append(ans)
        return answer # Returns the answers to the queries
    
    def dfs(self, course, value, prereq, visit):
        # Note that we have found the path
        if course == value: 
            return True

        # We have not found the value
        if course in visit: 
            return False 
        visit.add(course) # Add to visit hash set

        any_path = False
        for prereq_course in prereq[course]: 
            # use bit-wise or to see if any one of the paths from the original course gets us to the prereq
            any_path = any_path | self.dfs(prereq_course, value, prereq, visit) 
        return any_path 
