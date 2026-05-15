from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        s_counts = Counter() 
        t_counts = Counter() 

        for i in range(len(s)): 
            s_counts[s[i]]+=1
            t_counts[t[i]]+=1
        return s_counts == t_counts

        