class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = [i for i in secret]
        guess = [i for i in guess]
        same_pos = 0
        diff_pos = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                same_pos+=1
                guess[i]='$'
                secret[i] = '&'
        for i,val in enumerate(secret):
            if val=='&':
                continue
            for j,v in enumerate(guess):
                if v=='$':
                    continue
                if val == v and i!=j:
                    diff_pos += 1
                    guess[j]='$'
                    break
        return str(same_pos) + 'A' + str(diff_pos) + 'B'
                    