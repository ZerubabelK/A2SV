class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.preArray = [(0, 0, 0)]
        self.times = times
        
        candidates = defaultdict(int)
        
        for i in range(len(persons)):
            candidates[persons[i]] += 1
            
            if self.preArray[-1][2] > candidates[persons[i]]:
                self.preArray.append((times[i], self.preArray[-1][1], self.preArray[-1][2]))
                
            else:
                self.preArray.append((times[i], persons[i], candidates[persons[i]]))

                
    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        min_time = -1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] > t:
                right = mid - 1
            else:
                min_time = mid
                left = mid + 1
                
        return self.preArray[min_time + 1][1]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)