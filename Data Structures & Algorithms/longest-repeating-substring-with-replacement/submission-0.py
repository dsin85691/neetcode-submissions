class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 2 X, 2 Y ==> 4 Y or 4 X 
        # 3 A, 1 B, 1A, 2 B --> 5A,1B

        # BCAAACAB --> BAAAAAAB --> AAA...A 
        # depends on the longest substring 

        long_l, long_r = 0, 0

        for l in range(len(s)): 
            r = l 
            while r < len(s) and s[l] == s[r]: 
                r+=1 
            print(l, r, s[l:r])
            if r-l  > long_r - long_l + 1: 
                long_l, long_r = l, r-1
        print(long_l, long_r)
        for i in range(k): 
            if long_l-1 > 0 and long_r+1 < len(s):
                if s[long_l-1] == s[long_r+1]: 
                    long_r += 1
                long_l += 1 

        res = 0
        count = {}
        l = 0
        max_f = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])
            
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res