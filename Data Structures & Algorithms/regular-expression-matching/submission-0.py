class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)

        # dp[i][j] = s[:i] matches p[:j]
        dp = [[False] * (M + 1) for _ in range(N + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Patterns like a*, a*b*, a*b*c* can match empty string
        for j in range(2, M + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        for i in range(1, N + 1):
            for j in range(1, M + 1):

                # Case 1: normal character or '.'
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

                # Case 2: '*'
                elif p[j-1] == "*":
                    prev = p[j-2]

                    # Option 1: zero occurrences of prev*
                    dp[i][j] = dp[i][j-2]

                    # Option 2: one or more occurrences of prev*
                    if prev == "." or prev == s[i-1]:
                        dp[i][j] |= dp[i-1][j]

        return dp[N][M]