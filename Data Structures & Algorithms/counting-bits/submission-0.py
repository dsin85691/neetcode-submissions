class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [] 
        for i in range(0, n+1): 
            output.append(self.count1sForNum(i)) 
        return output
    
    def count1sForNum(self, n: int) -> int:
        count = 0 
        while n > 0: 
            if n & 1 == 1: 
                count+=1 
            n = n >> 1 
        return count