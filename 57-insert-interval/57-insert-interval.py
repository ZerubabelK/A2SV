class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag = True
        intervals.append(newInterval)
        for i in range(len(intervals)-2, -1, -1):
            if intervals[i][0] >= intervals[i + 1][0]:
                intervals[i][0], intervals[i + 1][0] = intervals[i + 1][0], intervals[i][0]
                intervals[i][1], intervals[i + 1][1] = intervals[i + 1][1], intervals[i][1]
            else:
                break
                
        if flag:
            intervals.append(newInterval)
            
        stack = []
        i = 0
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
                
            elif stack[-1][1] >= interval[0]:
                while stack and stack[-1][0] > interval[0]:
                    stack.pop()
                    
                stack[-1][0] = min(stack[-1][0], interval[0])
                stack[-1][1] = max(stack[-1][1], interval[1])
                
            else:
                stack.append(interval)
            
        return stack