class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False
        self.word = ""
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        for word in products:
            self.insert(word)
        for i in range(len(searchWord)):
            res.append(self.search(searchWord[:i + 1], 3))
        return res
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children.get(ch)
            
        curr.isend = True
        curr.word = word
        
    def search(self, pre, k):
        ans = []
        curr = self.root
        for ch in pre:
            if ch in curr.children:
                curr = curr.children.get(ch)
            else:
                return []
    
        def dfs(node):
            if node.isend:
                ans.append(node.word)

            for ch in node.children:
                dfs(node.children.get(ch))
                
        dfs(curr)

        return sorted(ans)[:k]