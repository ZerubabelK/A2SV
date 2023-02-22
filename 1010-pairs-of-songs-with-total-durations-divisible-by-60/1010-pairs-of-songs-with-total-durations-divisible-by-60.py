class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        seen = defaultdict(int)
        num_pairs = 0
        for num in time:
            complementary = 60 - num
            if complementary in seen:
                num_pairs += seen[complementary]
            if num == 0:
                num_pairs += seen[num]
            seen[num] += 1
        return num_pairs