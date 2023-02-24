class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        _dict = defaultdict(set)
        for id, t in logs:
            _dict[id].add(t)
        res = [0] * k
        for id in _dict:
            res[len(_dict[id]) - 1] += 1
        return res