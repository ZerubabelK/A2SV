class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i] - cost[i] for i in range(len(gas))]
        pre = [0]
        for val in net:
            pre.append(pre[-1] + val)
        curr = i = 0
        
        while i < len(gas):
            if net[i] >= 0:
                j = i
                while j < len(gas) and curr >= 0:
                    curr += net[j]
                    j += 1
                
                if j == len(gas) and curr + pre[i] >= 0:
                    return i
                
                curr = 0
                i = j
            else:
                i += 1
        return -1