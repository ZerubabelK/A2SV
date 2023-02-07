class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx, dy = 0, 1
    
        for ch in instructions:
            if ch == 'L':
                dx, dy = -dy, dx
                
            elif ch == 'G':
                x += dx
                y += dy
            else:
                dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)