class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isnumeric():
                digit.append(log)
            else:
                letter.append(log)
        if len(letter)>1:
            letter.sort(key = lambda log:(log.split()[1:], log.split()[0]))
            
        for dig in digit:
            letter.append(dig)
            
        return letter