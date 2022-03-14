class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        in_bound = lambda i: 0 <= i < len(arr)
        queue = collections.deque()
        visited = set()
        
        queue.append(start)
        visited.add(start)
        while queue:
            index = queue.popleft()
            
            if arr[index] == 0:
                return True
            
            if in_bound(index + arr[index]) and index + arr[index] not in visited:
                queue.append(index + arr[index])
                visited.add(index + arr[index])
                
            if in_bound(index - arr[index]) and index - arr[index] not in visited:
                queue.append(index - arr[index])
                visited.add(index + arr[index])
                
        return False