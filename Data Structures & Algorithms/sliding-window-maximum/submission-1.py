class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = Counter()
        n = len(nums)
        max_elem = -float("inf")
        max_window_step = []

        for i in range(k): 
            count[nums[i]] += 1
            if nums[i] > max_elem: 
                max_elem = nums[i] 
        
        max_window_step.append(max_elem)

        l = 0
        for r in range(k, n): 
            count[nums[r]] += 1
            count[nums[l]] -= 1 
            if nums[r] > max_elem: 
                max_elem = nums[r]
            elif count[max_elem] == 0: 
                max_elem = max([elem for elem in count if count[elem] > 0]) 
            max_window_step.append(max_elem)
            l += 1
        return max_window_step