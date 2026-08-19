class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_total = sum(nums)
        if sum_total % k != 0:
            return False
        sum_per_subset = sum_total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        memo = {}

        def dfs(k_remaining, current_sum, start_index):
            if k_remaining == 0:
                return True
            state = (tuple(used), k_remaining)
            if state in memo:
                return memo[state]
            if current_sum == sum_per_subset:
                res = dfs(k_remaining - 1, 0, 0)
                memo[state] = res
                return res

            for i in range(start_index, len(nums)):
                if not used[i] and current_sum + nums[i] <= sum_per_subset:
                    used[i] = True
                    if dfs(k_remaining, current_sum + nums[i], i + 1):
                        return True
                    used[i] = False
            memo[state] = False
            return False

        return dfs(k, 0, 0)