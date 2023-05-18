class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rank = [1] * n
        parent = {i:[i, float('inf')] for i in range(n)}
        def find(node):
            if parent[node][0] == node:
                return node
            parent[node][0] = find(parent[node][0])
            return parent[node][0]
        
        def union(node1, node2, distance):
            p_node1 = find(node1)
            p_node2 = find(node2)
            if p_node1 != p_node2:
                if rank[p_node1] > rank[p_node2]:
                    parent[p_node2][0] = p_node1
                    parent[p_node1][1] = min(parent[p_node1][1], parent[p_node2][1], distance)
                    rank[p_node1] += rank[p_node2]
                else:
                    parent[p_node1][0] = p_node2
                    parent[p_node2][1] = min(parent[p_node2][1],parent[p_node1][1], distance)
                    rank[p_node2] += rank[p_node1]
            else:
                parent[p_node1][1] = min(parent[p_node1][1], distance)
        for src, dst, dis in roads:
            union(src-1, dst-1, dis)
        
        return parent[find(0)][1]