class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2):
                return False

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False

            j = 0
            for i in range(len(s2) - len(s1), len(s2)):
                if s1[j] != s2[i]:
                    return False
                j += 1

            return True

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                res += isPrefixAndSuffix(words[i], words[j])
        return res