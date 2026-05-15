class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {} 

        for num in nums: 
            freq_map[num] = 1 + freq_map.get(num, 0) 

        sorted_map = sorted([(key,freq_map[key]) for key in freq_map.keys()], key=lambda x: x[1])

        return [val1 for val1, val2 in sorted_map[len(freq_map)-k:]]