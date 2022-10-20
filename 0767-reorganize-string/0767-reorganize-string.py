class Solution:
    def reorganizeString(self, s: str) -> str:
        heapList = self.heapifiedList(Counter(s).items())
        curr = ''
        res = ''
        while heapList:
            top = heappop(heapList)
            if top[1] == curr and heapList:
                rep, top = top, heappop(heapList)
                heappush(heapList, rep)
                
            elif top[1] == curr and not heapList:
                return ''
            
            curr = top[1]
            res += top[1]
            if top[0] < -1:
                heappush(heapList, (top[0] + 1, top[1]))
                
        return res
            
    
    def heapifiedList(self, pairs):
        array = [(-b, a) for a, b in pairs]
        heapify(array)
        return array