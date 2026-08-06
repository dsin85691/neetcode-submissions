class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unseen, seen = set([n for n in range(1, len(nums) + 1)]), set()
        for i in range(len(nums)): # O(n)
            if nums[i] not in seen: 
                seen.add(nums[i]) 
        return list(unseen - seen)

