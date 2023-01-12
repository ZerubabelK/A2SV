def maxKelements(self, nums: List[int], k: int) -> int:
    nums = [-v for v in nums]
    heapify(nums)
    score = 0
    for _ in range(k):
        v = heappop(nums)
        score -= v
        heappush(nums, -ceil(-v / 3))
    return score
