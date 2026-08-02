class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): 
            return False 
        
        # Equal length sentences
        # O(m)
        similar_map = collections.defaultdict(set) 
        for i in range(len(similarPairs)): 
            similar_map[similarPairs[i][0]].add(similarPairs[i][1]) 
            similar_map[similarPairs[i][1]].add(similarPairs[i][0]) 

        # O(n) 
        for i in range(len(sentence1)): 
            if sentence1[i] == sentence2[i] or sentence2[i] in similar_map[sentence1[i]]:
                continue
            return False
        return True