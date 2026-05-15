class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) > len(t) or len(s) < len(t): 
            return False

        s_anagram_dict = {} 
        t_anagram_dict = {} 

        for i in range(len(s)): 
            if s[i] not in s_anagram_dict: 
                s_anagram_dict[s[i]] = 1 
            else: 
                s_anagram_dict[s[i]]+=1

        for i in range(len(t)): 
            if t[i] not in t_anagram_dict: 
                t_anagram_dict[t[i]] = 1
            else: 
                t_anagram_dict[t[i]]+=1

        for key in s_anagram_dict.keys(): 
            if key not in t_anagram_dict.keys(): 
                return False 
            if s_anagram_dict[key] != t_anagram_dict[key]: 
                return False 

        return True
        

            
        