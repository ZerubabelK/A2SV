class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        heapify(stones)
        i = 0
        while len(stones) > 1:   
            if len(stones) > 2:
                toPop = -1
                if stones[2*i+1] < stones[2*i+2]:
                    toPop = 2*i+1
                else:
                    toPop = 2*i+2
                x = min(stones[2*i+1], stones[2*i+2])
                y = stones[i]
                if x != y:
                    stones[i] = y - x
                    stones.pop(toPop)
                else:
                    stones.pop(toPop)
                    stones.pop(0)
            else:
                if  stones[1] != stones[0]:
                    stones[i] = stones[0] - stones[1]
                    stones.pop(1)
                else:
                    stones.pop(1)
                    stones.pop(0)
            heapify(stones)
        
        if len(stones) > 0:
            return stones[0] * -1
        else:
            return 0