class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {letter:i for i,letter in enumerate(s)}
        
        first, last = 0, 0
        
        partitions = []
        
        for i, letter in enumerate(s):
            
            last = max(last_indices[letter], last)
            
            if i == last:
                
                partitions += [last - first + 1]
            
                first = i + 1

        return partitions