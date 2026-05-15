class Solution:
    def reverseBits(self, n: int) -> int:
        
        bit_place = 31 
        val = 0  

        while n > 0: 
            if n & 1 == 1: 
                val += (2 ** bit_place)               
            n = n >> 1 
            bit_place-=1 
        
        return val