class TrieNode:
    def __init__(self, val = ''):
        self.val = val
        self.children = {}
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        arr = sentence.split(' ')
        for i in range(len(arr)):
            arr[i] = self.searchRoot(arr[i])

        return ' '.join(arr)
        
    def searchRoot(self, word: str) -> str:
        it = self.root
        strs = ''
        for l in word:
            if l in it.children:
                strs += l
                it = it.children[l]
            else:
                break
                
            if it.isEnd:
                return strs
        return word
                
    def insert(self, word: str) -> None:
        it = self.root
        for l in word:
            if l not in it.children:
                it.children[l] = TrieNode(l)
            
            it = it.children[l]
        it.isEnd = True