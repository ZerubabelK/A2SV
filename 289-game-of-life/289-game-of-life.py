class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """   
        changed = set()
        n, m = len(board), len(board[0])
        inbound = lambda row, col: 0 <= row < n and 0 <= col < m
        DIR = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        for i in range(n):
            for j in range(m):
                lives = 0
                for d in DIR:
                    row, col = i + d[0], j + d[1]
                    
                    if not inbound(row, col):
                        continue
                    
                    if (row, col) not in changed:
                        lives += board[row][col]
                    
                    else:
                        lives += 1 if board[row][col] == 0 else 0
                        
                if lives < 2 and board[i][j] == 1:
                    board[i][j] = 0
                    changed.add((i,j))
                elif lives == 3 and board[i][j] == 0:
                    board[i][j] = 1
                    changed.add((i,j))
                elif lives > 3 and board[i][j] == 1:
                    board[i][j] = 0
                    changed.add((i,j))