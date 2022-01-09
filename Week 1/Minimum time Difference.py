class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [i.split(':') for i in timePoints]
        newTime = [] * len(timePoints)
        for i in timePoints:
            mins = int(i[0]) * 60 + int(i[1])
            # if mins==0:
            #     mins = 1440
            newTime.append(mins)
        minT = 720
        m = [abs(newTime[i] - newTime[j]) for i in range(len(newTime)) for j in range(i+1,len(newTime))]   
        m = [1440 - i if i>720 else i for i in m]
        m.sort()
        return m[0]