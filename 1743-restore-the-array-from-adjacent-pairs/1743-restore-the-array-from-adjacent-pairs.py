class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def buildArray(value):
            for adj in adjacents[value]:
                if adj in seen:
                    continue
                array.append(adj)
                seen.add(adj)
                buildArray(adj)
        
        adjacents = defaultdict(list)
        for a, b in adjacentPairs:
            adjacents[b].append(a)
            adjacents[a].append(b)
        array = []
        seen = set()
        for key in adjacents:
            if len(adjacents[key]) == 1:
                array.append(key)
                seen.add(key)
                buildArray(key)
                break
                
        return array
    