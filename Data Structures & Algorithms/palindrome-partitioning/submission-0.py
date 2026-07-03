class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        path = []
        self.helper(0, s, path, res)
        return res 

    def helper(self, i, s, path, res):
        if i == len(s):
            res.append(path[:])
            return

        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                path.append(s[i:j+1])       # Choose
                self.helper(j + 1, s, path, res)  # Explore
                path.pop()                  # Unchoose


    def isPalindrome(self, p, l, r): 
        while l < r: 
            if p[l] != p[r]: 
                return False
            l+=1
            r-=1 
        return True