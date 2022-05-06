class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = [sorted(list(word)) for word in strs]
        anagrams = defaultdict(list)
        
        for i in range(len(arr)):
            anagrams[''.join(arr[i])].append(strs[i])
            
        return anagrams.values()
        