class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        arr = []
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                arr.append(i)
        return len(arr)