class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        while tickets[k]:
            for i in range(k+1):
                if tickets[i]:
                    tickets[i]-=1
                    time+=1
            if tickets[k]:
                for i in range(k+1,len(tickets)):
                    if tickets[i]:
                        tickets[i]-=1
                        time+=1
        return time