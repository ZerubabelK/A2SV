class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(str(int(''.join([str(digit) for digit in num])) + k))