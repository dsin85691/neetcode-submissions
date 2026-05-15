class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                # The minimum is in the right half
                L = mid + 1
            else:
                # The minimum is in the left half (including mid)
                R = mid
        
        # L and R will converge to the minimum element
        return nums[L]