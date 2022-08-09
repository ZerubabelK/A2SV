class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key = lambda interval: interval[0])
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            
            if stack[-1][1] >= interval[0]:
                while stack and stack[-1][0] > interval[0]:
                    stack.pop()
                stack[-1][0] = min(stack[-1][0], interval[0])
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)
                
        return stack