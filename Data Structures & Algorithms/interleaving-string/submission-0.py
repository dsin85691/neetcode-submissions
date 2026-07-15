class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            if i == len(s1) and j == len(s2):
                return True

            ans = False

            # Take from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                ans |= dfs(i + 1, j)

            # Take from s2
            if not ans and j < len(s2) and s2[j] == s3[i + j]:
                ans |= dfs(i, j + 1)

            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)