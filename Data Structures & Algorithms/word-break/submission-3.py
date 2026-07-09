class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            # Reached the end
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            for word in wordDict:
                # Does this word match starting at index i?
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        cache[i] = True
                        return True

            cache[i] = False
            return False

        return dfs(0)