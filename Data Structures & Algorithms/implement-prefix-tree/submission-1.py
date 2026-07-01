class Node: 
    def __init__(self, prefix=""): 
        self.prefix = prefix
        self.word = False
        self.children = [] 

class PrefixTree:

    def __init__(self):
        self.root = Node() 

    def insert(self, word: str) -> None:
        tmp = self.root 
        idx = 0 
        while idx < len(word):
            found_prefix = False
            new_node = None
            for child in tmp.children: 
                if child.prefix == word[idx]: 
                    found_prefix = True 
                    new_node = child

            if found_prefix: 
                tmp = new_node # Change it to the child node
            else: 
                new_node = Node(prefix=word[idx]) # Create a new node
                tmp.children.append(new_node) # Append the new node to the end of the trie
                tmp = new_node
            idx+=1 # Increment to next char in word
        tmp.word = True # Mark the word as true within its place within the trie
            

    def search(self, word: str) -> bool:
        tmp = self.root 
        idx = 0 
        while idx < len(word): 
            new_tmp = None
            for child in tmp.children: 
                if child.prefix == word[idx]: 
                    new_tmp = child 
            if new_tmp is None:
                return False
            tmp = new_tmp
            idx += 1 # Increment to the next char in the word
        return True if tmp.word else False # Check if it is a word or not
            
    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for char in prefix: 
            new_tmp = None
            for child in tmp.children: 
                if child.prefix == char: 
                    new_tmp = child 
            if new_tmp is None: 
                return False 
            else: 
                tmp = new_tmp
        return True
        
        