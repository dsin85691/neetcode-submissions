class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = ans = nums[0]

        for num in nums[1:]:
            candidates = (
                num,
                num * curr_max,
                num * curr_min
            )

            curr_max = max(candidates)
            curr_min = min(candidates)

            ans = max(ans, curr_max)

        return ans