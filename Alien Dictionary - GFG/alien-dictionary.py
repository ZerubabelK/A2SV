#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # print(alien_dict)
        for i in range(len(alien_dict)-1):
            edge = self.compareStrings(alien_dict[i], alien_dict[i+1], indegree)
            if edge:
                graph[edge[0]].append(edge[1])
                indegree[edge[0]] = 0 if edge[0] not in indegree else indegree[edge[0]]
                indegree[edge[1]] += 1
        queue = deque()
        for i in range(k):
            if not indegree[chr(ord('a') + i)]:
                queue.append(chr(ord('a') + i))
        order = []
        while queue:
            letter = queue.popleft()
            order.append(letter)
            for neigh in graph[letter]:
                indegree[neigh] -= 1 if indegree[neigh] else 0
                if not indegree[neigh]:
                    queue.append(neigh)
        return ''.join(order)
        
    def compareStrings(self, string1, string2, indegree):
        i = j = 0
        while i < len(string1) and j < len(string2):
            if string1[i] != string2[j]:
                return (string1[i], string2[j])
            i += 1
            j += 1
            
        
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends