class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]

        print(suffix)

        cache = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in cache:
                return cache[(i, M)]

            best = 0

            # take x piles
            for x in range(1, min(2*M, n-i) + 1):
                # stones Alice takes now
                taken = suffix[i] - suffix[i+x]

                # Bob gets the optimal remainder
                bob = dp(i+x, max(M, x))

                # Alice gets everything remaining minus Bob
                best = max(best, taken + (suffix[i+x] - bob))

            cache[(i, M)] = best
            return best

        return dp(0, 1)