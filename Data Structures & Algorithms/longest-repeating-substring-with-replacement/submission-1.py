class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 2 X, 2 Y ==> 4 Y or 4 X 
        # 3 A, 1 B, 1A, 2 B --> 5A,1B

        # BCAAACAB --> BAAAAAAB --> AAA...A 
        # depends on the longest substring 

        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res