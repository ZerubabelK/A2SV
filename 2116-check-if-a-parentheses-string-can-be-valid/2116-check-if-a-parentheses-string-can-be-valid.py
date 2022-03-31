class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        balance = 0
        for i in range(len(s)):
            balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            if balance < 0:
                return False

        balance = 0
        for i in range(len(s) - 1, -1, -1):
            balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            if balance < 0:
                return False

        return True