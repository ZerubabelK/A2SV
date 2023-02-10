class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dictA, dictB  = {}, {}
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1: 
                    dictA[(i,j)] = 1
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1: 
                    dictB[(i,j)] = 1
                    
        dict3 = {}
        for ra, ca in dictA:
            for rb, cb in dictB:
                shift = (rb - ra, cb - ca)
                if shift not in dict3: 
                    dict3[shift] = 1
                else: 
                    dict3[shift] += 1
                    
        ans = 0
        for key in dict3:
            ans = max(ans, dict3[key])
        return ans