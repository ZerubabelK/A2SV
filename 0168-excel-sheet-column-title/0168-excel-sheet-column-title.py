class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        characters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        string = []
        while columnNumber > 0:
            string.append(characters[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        return ''.join(string[::-1])