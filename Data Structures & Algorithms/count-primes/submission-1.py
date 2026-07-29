class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * n
        res = 0
        for num in range(2, n):
            if not sieve[num]:
                res += 1
                for i in range(num * num, n, num):
                    sieve[i] = True
        return res