class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        t = 0 # time (or turn)
        aliceSum, bobSum = 0, 0 # Sum so far
        l, r = 0, len(piles) - 1 # Starting points for both
        cache = {} # cache / memo

        return self.stoneThink(t, l, r, piles, aliceSum, bobSum, cache)

    # O(2^n) where n  is the length of the piles (Original solution), space complexity O(h) = O(n) 
    # O(2^n) --> Caching --> O(L * R) = O((n/2) * (n/2)) = O(n^2 / 4) = O(n^2), space complexity O(n^2)
    # Time Complexity O(n^2) 
    def stoneThink(self, t, l, r, piles, aliceSum, bobSum, cache):
        # caching (top-down DP) 
        if (l,r) in cache: 
            return cache[(l,r)] 

        # Base case is when all remaining piles are taken
        if l >= r: 
            return aliceSum > bobSum 

        # two choices l, r 
        if t % 2 == 0: 
            aliceSum += piles[l]
        else: 
            bobSum += piles[l]

        left_start = self.stoneThink(t + 1, l + 1, r, piles, aliceSum, bobSum, cache) 
        cache[(l,r)] = left_start # Make sure to cache result for future

        # Restore the sum prior to recursive call
        if t % 2 == 0: 
            aliceSum -= piles[l] # Restore value
            aliceSum += piles[r] # Add in new value
        else: 
            bobSum -= piles[l] # restore value 
            bobSum += piles[r] # Add in new value

        right_start = self.stoneThink(t + 1, l, r - 1, piles, aliceSum, bobSum, cache)
        cache[(l,r)] = right_start
        
        # Check if Alice wins (optimally) from either branch
        return left_start | right_start
