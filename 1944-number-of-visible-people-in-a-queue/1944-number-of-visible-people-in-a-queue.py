class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                index = stack.pop()
                answer[index] += 1
                if stack:
                    answer[stack[-1]] += 1
            stack.append(i)
        for i in range(len(stack)-1):
            answer[stack[i]] += 1
        return answer