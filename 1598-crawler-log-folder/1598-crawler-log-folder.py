class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log not in set(["../", "./"]):
                stack.append(log)
            elif log == "../" and len(stack) > 0:
                stack.pop()
        return len(stack)