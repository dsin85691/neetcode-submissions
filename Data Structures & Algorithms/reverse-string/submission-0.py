class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1 
        while i < j: 
            left_ch, right_ch = s[i], s[j] 
            s[j], s[i] = left_ch, right_ch 
            i+=1
            j-=1