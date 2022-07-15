class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = defaultdict(list)
        for num in nums:
            strs = str(num)
            strs1 = ''
            for digit in strs:
                strs1 += str(mapping[int(digit)])
            mapped[int(strs1)].append(num)
        keys = sorted(mapped.keys())
        ans = []
        for key in keys:
            ans += mapped[key]
        return ans