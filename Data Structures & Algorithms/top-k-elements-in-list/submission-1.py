class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for i in range(len(nums)): 
            if nums[i] not in freq: 
                freq[nums[i]] = 1 
            else: 
                freq[nums[i]]+=1 

        print(freq) 

        freq_list = [(key, val) for key,val in zip(freq.keys(), freq.values())]

        print(freq_list) 

        freq_list = sorted(freq_list, key=lambda x: x[1]) 

        print(freq_list) 

        topK = [] 

        for i in range(len(freq_list)-1, len(freq_list)-k-1, -1): 
            topK.append(freq_list[i][0])

        return topK