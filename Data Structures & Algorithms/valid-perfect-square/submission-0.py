class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r: 
            mid = (l + r) // 2 
            res = mid * mid

            if res == num:
                return True
            elif res < num: 
                l = mid + 1
            else: 
                r = mid - 1
        return False