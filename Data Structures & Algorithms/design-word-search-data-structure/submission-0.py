class Node: 
    def __init__(self): 
        self.word     = False
        self.children = {}



class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.word = True
                
    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.word

            ch = word[idx]

            if ch == ".":
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(idx + 1, node.children[ch])

        return dfs(0, self.root)