class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num // 3
        if middle * 3 == num:
            return [middle-1, middle, middle + 1]
        else:
            return []