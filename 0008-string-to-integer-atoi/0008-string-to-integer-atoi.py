class Solution:
    def myAtoi(self, s: str) -> int:
        def stripWhiteSpaces(num: str) -> str:
            j = 0
            while j < len(num) and num[j] == ' ':
                j += 1
            return num[j:]
        def getSign(num: str) -> int:
            if num and num[0] == '-':
                return -1
            if num and num[0] == '+':
                return 0
            return 1
        def stripLeadingZero(num: str) -> str:
            j = 0
            while j < len(num) and num[j] == '0':
                j += 1
            return num[j:]
        def getInteger(num: str) -> int:
            j = 0
            while j < len(num) and num[j].isdigit():
                j += 1
            return int(num[:j]) if j > 0 else 0
        s = stripWhiteSpaces(s)
        sign = getSign(s)
        if sign < 0:
            s = s[1:]
        if sign == 0:
            s = s[1:]
            sign = 1
        s = stripLeadingZero(s)
        num = getInteger(s)
        if sign * num > 2 ** 31 - 1:
            return 2**31 - 1
        elif sign * num < -2 ** 31:
            return -2 ** 31
        return num * sign
            