class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag = True
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                    intervals.insert(i, newInterval)
                    flag = False
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
                
        # if not stack:
        #     stack.append(newInterval)
            
        return stack