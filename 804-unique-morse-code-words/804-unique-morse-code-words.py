class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:        
        unique = set()
        
        for word in words:
            unique.add(self.transform(word))
        
        return len(unique)
            
    def transform(self, word: str) -> str:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        strs = []
        for ch in word:
            i = ord(ch) - 97
            strs.append(morse[i])
            
        return ''.join(strs)