class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([[0,1]])
        moves = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                pos, speed = queue.popleft()
                if pos == target:
                    return moves

                queue.append([pos + speed, speed * 2])
                if (pos + speed < target and speed < 0) or (pos + speed > target and speed > 0):
                    queue.append([pos, -1 if speed > 0 else 1])
            moves += 1
            
        return moves