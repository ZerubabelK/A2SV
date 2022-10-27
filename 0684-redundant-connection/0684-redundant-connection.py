class Solution:
    def __init__(self):
        self.parent = {}
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.makeset(len(edges))
        for u, v in edges:
            if self.union(u, v):
                return [u, v]
        
    def makeset(self, nodes):
        for node in range(nodes):
            self.parent[node + 1] = node + 1
    def find(self, curr_node):
        while curr_node != self.parent[curr_node]:
            curr_node = self.parent[curr_node]

        return curr_node

    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent == v_parent:
            return True
        else:
            self.parent[u_parent] = v_parent
        return False
    
        