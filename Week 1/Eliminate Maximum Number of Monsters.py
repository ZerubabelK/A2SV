class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        z = list(zip(dist,speed))
        z.sort(key = lambda el: (1/el[1],el[0]-el[1]))
        print(z)
        dist = [el[0] for el in z]
        speed = [el[1] for el in z]
        for i in range(len(dist)):
            if all(dist) == False:
                break
            dist[i] = 'X'
            for j in range(i+1,len(dist)):
                dist[j] -= speed[j]
                if dist[j]<=0:
                    dist[j] = 0
        return len([j for j in dist if j=='X'])